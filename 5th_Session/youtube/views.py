# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404, redirect
from .models import Video

# Create your views here.
def detail(request,detail_id):
    detail = get_object_or_404(Video, pk=detail_id)
    return render(request,'detail.html',{'content':detail})

def home(request):
    videos = Video.objects
    return render(request,'home.html',{'videos':videos})

def create(request):
    Youtube = Video()
