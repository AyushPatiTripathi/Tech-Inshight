from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse 
from .models import Blogpost
from django.core.paginator import Paginator
from django.db.models import Q


def blog(request):
    query = request.GET.get("q","").strip()
    posts = Blogpost.objects.all().order_by('-created_at') # newest  f[irst
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__icontains=query)
    )
 
    
    paginator = Paginator(posts , 5)
    
    page_number = request.GET.get('page')
    posts_ = paginator.get_page(page_number)
    return render(request,'blog/blog.html',{'posts': posts_,
                                            'query': query})
    
def blog_detail(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    return render(request, 'blog/detail.html', {'post':post})
    


