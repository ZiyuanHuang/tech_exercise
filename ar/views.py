from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_list(request):
	posts = Post.objects.all()
	#selectedPost = ...
	return render(request, 'ar/post_list.html', {'posts': posts,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'ar/post_detail.html', {'post': post})