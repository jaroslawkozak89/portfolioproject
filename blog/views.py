from django.shortcuts import render, get_object_or_404

from .models import Blog

def blog_main(request):
    blogs = Blog.objects.order_by('-blog_pub_date')
    return render(request, 'blog/blog_main.html', {'blogs':blogs})

def blog_detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog':detailblog})
