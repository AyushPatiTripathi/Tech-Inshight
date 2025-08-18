from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse 
from .models import Blogpost
from django.core.paginator import Paginator



def blog(request):
    posts_list = Blogpost.objects.all().order_by('-created_at') # newest  f[irst
  
    
    paginator = Paginator(posts_list , 5)
    
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request,'blog/blog.html',{'posts': posts})
    
def blog_detail(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    return render(request, 'blog/detail.html', {'post':post})


