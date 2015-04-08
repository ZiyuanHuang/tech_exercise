from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'ar/post_list.html', {'posts': posts})
