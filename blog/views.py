from django.shortcuts import render, get_object_or_404 #for get the blog number if not show 404 error
from .models import Blog

def all_blogs(request):
	blogs = Blog.objects.order_by('-date')#[:5] #use "order_by(-date)" to sorted by date and show latest blog & "[:5]" to show 5 blogs
	return render(request,'blog/all_blogs.html', {'blogs':blogs})

def detail(request,blog_id):
	blog = get_object_or_404(Blog, pk=blog_id) #show the Blog model by its pk or 'primary key' if mot show 404 error
	return render(request, 'blog/detail.html', {"blog":blog})