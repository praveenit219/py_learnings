from django.db import models

# Create your models here.

class Destination(models.Model):
  
    name = models.CharField(max_length=40)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.FloatField()
    offer = models.BooleanField()
