from django.shortcuts import render
from .models import Blog

def all_blogs(request):
	blogs = Blog.objects.order_by('-date')[:5] #use "order_by(-date)" to sorted by date and show latest blog & "[:5]" to show 5 blogs
	return render(request,'blog/all_blogs.html', {'blogs':blogs})