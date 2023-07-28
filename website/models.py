from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    
