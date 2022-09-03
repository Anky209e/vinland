from django.db import models


class ImageModel(models.Model):
    image_field = models.ImageField(upload_to="model_images/")