from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User

class index(ListView):
    template_name = 'index.html'
    context_object_name = 'blog_list' 
    def get_queryset(self):
        return Blog.objects.all

class detail(DetailView):
    model = Blog
    template_name = 'detail.html'
    context_object_name = 'blog'

class delete(DeleteView):
    model = Blog
    template_name = 'delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('index')

class update(UpdateView):
    model = Blog
    template_name = 'update.html'
    fields = ['title','text']
    success_url = reverse_lazy('index')

class create(CreateView):
    model=Blog
    template_name='create.html'
    fields=['title','text']

    def form_valid(self,form):
        Blog=form.save(commit=False)
        Blog.author=self.request.user
        Blog.save()

        return HttpResponseRedirect(self.request.POST.get('next','/'))

def result(request):
   BlogPosts = Blog.objects.all()
   query = request.GET.get('query', '')
   howtoselect = request.GET.get('howtoselect', '')
    
   if howtoselect=="all":
       BlogPosts = BlogPosts.filter(Q(title__icontains=query)| Q(text__icontains=query)).order_by('-time')

        
   elif howtoselect=="title":
        BlogPosts = BlogPosts.filter(Q(title__icontains=query)).order_by('-time')

        
   elif howtoselect=="text":
        BlogPosts = BlogPosts.filter(Q(text__icontains=query)).order_by('-time')

        
   elif howtoselect=="author":
        BlogPosts = BlogPosts.filter(Q(author__icontains=query)).order_by('-time')


   return render(request, 'result.html', {'BlogPosts':BlogPosts, 'query':query,  'howtoselect':howtoselect})
