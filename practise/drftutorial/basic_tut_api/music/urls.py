from django.urls import path, register_converter
from .views import ListSongsView, SongsDetailView, ListCreateSongsView, LoginView, RegisterView
from django.urls.converters import register_converter
from .CustomConverters import NegativeIntConverter

register_converter(NegativeIntConverter, 'negint')

urlpatterns = [
    #path('songs/', ListSongsView.as_view(), name='songs-all'),
    path('songs/', ListCreateSongsView.as_view(), name='songs-list-create'),
    path('songs/<negint:pk>', SongsDetailView.as_view(), name='songs-detail'),
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/register/', RegisterView.as_view(), name='auth-register'),

]