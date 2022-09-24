from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250)
    avatar = models.ImageField(upload_to = 'profile_images/', default='profile_images/avatar.png')
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELD = ['username']
    