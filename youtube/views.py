# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Video

# Create your views here.

def home(request):
    videos = Video.objects
    return render(request,'home.html',{'videos':videos})