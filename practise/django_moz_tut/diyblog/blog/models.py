from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.
class Blog(models.Model):
    name = models.CharField(
            max_length = 100,
            help_text = 'Enter Blog Name'
            )
    author = models.ForeignKey('BlogAuthor', on_delete = models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the blog")
    post_date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class BlogAuthor(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text="Enter a brief introuduction of your bio")

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.name.username


class BlogComment(models.Model):
    description = models.TextField(max_length=1000, help_text="you can enter comments of upto 1000 chars")
    post_date = models.DateTimeField(auto_now_add=True , null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)

    def __str__(self):
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring