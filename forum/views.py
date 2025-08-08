from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(draft=False).order_by('-created_at')
    return render(request, 'forum/post_list.html', {'posts': posts})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category, draft=False)
    return render(request, 'forum/category_detail.html', {'category': category, 'posts': posts})