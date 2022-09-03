from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to="profile_images", null=True)
    prev_dets = models.TextField()

    def __str__(self):
        return str(self.user)
    

# Create your models here.
