# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
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
    Youtube.channel=request.POST['name']
    Youtube.name=request.POST['creator']
    Youtube.sub=request.POST['subscribe_num']
    Youtube.linkone=request.POST['youtube_link_1']
    Youtube.linktwo=request.POST['youtube_link_2']
    Youtube.linkthree=request.POST['youtube_link_3']
    Youtube.summary=request.POST['summary']
    Youtube.text=request.POST['text']
    Youtube.livecast=request.POST['choices']
    Youtube.save()
    return redirect('home')

def new(request):
    return render(request,'new.html')