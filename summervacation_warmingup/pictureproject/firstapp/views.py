from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import photo


def home(request):
    photo_obj = photo.objects
    return render(request, 'home.html',{"home_key":photo_obj})

def detail(request, detail_id):
    detail_obj = get_object_or_404(photo, pk=detail_id)
    return render(request, 'detail.html', {"detail_key":detail_obj})

def create(request):
    if request.method == "POST":
        photo_val = photo()
        photo_val.name = request.POST.get('name')
        photo_val.reason = request.POST.get('reason')
        photo_val.date = request.POST.get('date')
        photo_val.pic = request.FILES.get('pic')
        photo_val.save()
        return redirect(reverse('home'))
    else:
        pass
    return render(request,'create.html')

def update(request, update_id):
    update_obj=get_object_or_404(photo, pk=update_id)
    if request.method == "POST":
        update_obj.name = request.POST['name']
        update_obj.reason = request.POST['reason']
        update_obj.date = request.POST['date']
        update_obj.save()
        return redirect('home')
    else:
        pass
    return render(request,'update.html',{"update_key":update_obj})

def delete(request, delete_id):
    delete_obj = get_object_or_404(photo, pk=delete_id)
    delete_obj.delete()
    return redirect('home')
