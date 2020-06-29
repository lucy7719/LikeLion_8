from django.shortcuts import render,get_object_or_404,redirect
from .models import introduce
# Create your views here.
def detail(request,detail_id):
    detail = get_object_or_404(introduce,pk=detail_id)
    return render(request,'detail.html',{'content':detail})

def home(request):
    intro = introduce.objects
    return render(request,'home.html',{'intro':intro})

def new(request):
    form = createForm()
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = createFrom()
        return render(request,'new.html',{'form':form})
    else:
        pass

def create(request):
    introduce.photo = request.FILES['photo']
    introduce.save()
    return redirect('develop')