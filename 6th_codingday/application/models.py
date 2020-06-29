from django.db import models

# Create your models here.

class introduce(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="image",blank=True)