from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse 
from .models import Blogpost


def blog(request):
    posts = Blogpost.objects.all().order_by('-created_at') # newest  f[irst
    return render(request,'blog/blog.html',{'posts': posts})
    
def blog_detail(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    return render(request, 'blog/detail.html', {'post':post})


