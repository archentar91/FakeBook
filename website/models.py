from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    country = CountryField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=30)

    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    
