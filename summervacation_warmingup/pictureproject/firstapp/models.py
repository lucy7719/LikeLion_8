from django.db import models
from django import forms
from datetime import datetime

class UploadFileForm(forms.Form):
    titles = forms.CharField(max_length=100)
    file = forms.FileField()

class photo(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, default="작품 이름을 입력해 주세요")
    reason = models.TextField(default="이 작품을 선정한 이유는 무엇인가요?")
    pic = models.ImageField(upload_to="image", blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

