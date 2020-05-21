# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Video (models.Model):
    channel = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    preference = models.IntegerField()
    livecast = models.BooleanField()
    sub = models.IntegerField()
    linkone = models.TextField()
    linktwo = models.TextField()
    linkthree = models.TextField()