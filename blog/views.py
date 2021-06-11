from django.shortcuts import render

def all_blogs(request):
	return render(request,'blog/all_blogs.html')
