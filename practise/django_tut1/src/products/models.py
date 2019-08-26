from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60) #max_length required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False) #default='this is cool!' you can have like this set
    featured = models.BooleanField(default=False) #null=True, default=True this will let old entries to be set as empty or just choose 1 in migrations

    def get_absolute_url(self):
        #return f"/products/{self.id}/" 
        return reverse('products:product-specific', kwargs={'id': self.id}) #for dynamic url with reerse using view name for url mapings

