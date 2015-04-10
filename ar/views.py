from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from random import randint
from django.db.models import Count

def post_list(request):
	posts = Post.objects.all()
	posts = posts.order_by('published_date')
	n = randint(0,9)
	selectedPosts = posts[n]
	return render(request, 'ar/post_list.html', {'posts': posts, 'selectedPosts': selectedPosts,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # n = randint(0,9)
    # selectedPosts = posts[n]
    return render(request, 'ar/post_detail.html', {'post': post,})