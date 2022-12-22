from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    created_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)
    