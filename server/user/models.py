from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    fullName = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.fullName