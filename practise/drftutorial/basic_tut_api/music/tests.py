from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer
from django.contrib.auth.models import User


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def login_a_user(self, username="", password=""):
        url = reverse("auth-login", kwargs={
            "version": "v1"
        }
                      )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type='application/json'
        )

    def login_client(self, username="", password=""):
        response = self.client.post(
            reverse('create-token'),
            data=json.dumps(
                {
                    "username": username,
                    "password": password
                }
            ),
            content_type='application/json'
        )
        self.token = response.data['token']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test_user@pheonix.com",
            password="testing",
            first_name="test",
            last_name="user",
        )

        # add test data
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")
        self.valid_song_id = 1
        self.invalid_song_id = 100
        self.valid_data = {
            "title": "test a title",
            "artist": "testArtist"
        }
        self.invalid_data = {
            "title": "",
            "artist": ""
        }
        self.update_data = {
            "title": "test a title",
            "artist": "testUpdatedArtist"
        }
        self.update_invalid = {
            "title": "",
            "artist": ""
        }
        self.update_invalid_id = {
            "title": "test title2",
            "artist": "testUpdatedArtist2"
        }

    def fetch_a_song(self, pk=0):
        return self.client.get(
            reverse('songs-detail', kwargs={
                "version": "v1",
                "pk": pk
            }
                    )
        )

    def delete_a_song(self, pk=0):
        return self.client.delete(
            reverse('songs-detail', kwargs={
                "version": "v1",
                "pk": pk
            }
                    )
        )

    def make_a_request(self, kind="post", **kwargs):
        if kind == "post":
            return self.client.post(
                reverse('songs-list-create',
                        kwargs={
                            "version": kwargs["version"]
                        }
                        ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        elif kind == "put":
            return self.client.put(
                reverse('songs-detail',
                        kwargs={
                            "version": kwargs["version"],
                            "pk": kwargs["id"]
                        }
                        ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )
        else:
            return None


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        self.login_client('test_user', 'testing')
        response = self.client.get(
            # reverse("songs-all", kwargs={"version": "v1"})
            reverse('songs-list-create', kwargs={'version': 'v1'})
        )
        # fetch the data from db
        expected = Songs.objects.all()
        # print(response.data)
        serialized = SongsSerializer(expected, many=True)
        # print(serialized.data)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetASingleSongsTest(BaseViewTest):

    def test_get_a_song(self):
        response = self.fetch_a_song(self.valid_song_id)
        expected = Songs.objects.get(pk=self.valid_song_id)
        serialized = SongsSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.fetch_a_song(self.invalid_song_id)
        self.assertEqual(response.data["message"], "Song with id: 100 does not exist")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AddSongsTest(BaseViewTest):

    def test_create_a_song(self):
        self.login_client('test_user', 'testing')
        response = self.make_a_request(
            kind="post",
            version="v1",
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.make_a_request(
            kind="post",
            version="v1",
            data=self.invalid_data
        )
        self.assertEqual(response.data["message"], "Both title and artist are to add a song")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSongsTest(BaseViewTest):

    def test_update_a_song(self):
        self.login_client('test_user', 'testing')
        response = self.make_a_request(
            kind="put",
            version="v1",
            id=2,
            data=self.update_data
        )
        self.assertEqual(response.data, self.update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.make_a_request(
            kind="put",
            version="v1",
            id=3,
            data=self.update_invalid
        )
        self.assertEqual(
            response.data["message"],
            "Both title and artist are required to add a song"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        fetch_id = 56
        response = self.make_a_request(
            kind="put",
            version="v1",
            id=fetch_id,
            data=self.update_invalid_id
        )
        self.assertEqual(response.data["message"],
                         "Song with id: {} does not exist".format(fetch_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DeleteSongsTest(BaseViewTest):

    def test_delete_a_song(self):
        self.login_client('test_user', 'testing')
        response = self.delete_a_song(1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.delete_a_song(100)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AuthLoginUserTest(BaseViewTest):

    def test_login_user_with_valid_credentials(self):
        response = self.login_a_user("test_user", "testing")
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.login_a_user("anonymous", "pass")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthRegisterUserTest(BaseViewTest):

    def test_register_a_user_with_valid_data(self):
        url = reverse('auth-register',
                      kwargs={
                          "version": "v1"
                      }
                      )
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    "username": "new_user",
                    "password": "new_pass",
                    "email": "new_user@phoenix.com"
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_a_user_with_invalid_data(self):
        url = reverse('auth-register',
                      kwargs={
                        "version": "v1"
                      }
                      )
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    "username": "",
                    "password": "",
                    "email": ""
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)