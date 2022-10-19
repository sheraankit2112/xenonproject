from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class contactformdata(models.Model):
    name=models.CharField(max_length=20)
    contact=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    message=models.CharField(max_length=200)

class userbio(models.Model):
    name=models.CharField(max_length=20)
    
    mobile=models.IntegerField(max_length=20)
    email=models.EmailField(max_length=20)



