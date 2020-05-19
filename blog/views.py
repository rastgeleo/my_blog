from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Category
from .forms import PostForm, CategoryForm


def index(request):
    return render(request, 'blog/index.html')


def posts(request, category_id=None):
    """Show all blog posts"""
    if category_id:
        posts = Post.objects.filter(
            category_id=category_id
            ).order_by('-date_added')
    else:
        posts = Post.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blog/posts.html', context)


def post(request, post_id):
    """Detail view for a post"""
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'blog/post.html', context)


def categories(request):
    """Show all categories"""
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/categories.html', context)


@login_required
def new_post(request):
    """view to add a new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect('post', post_id=new_post.id)
    context = {'form': form}
    return render(request, 'blog/new_post.html', context)


@login_required
def new_category(request):
    """view to add a new category"""
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context = {'form': form}
    return render(request, 'blog/new_category.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post"""
    post = Post.objects.get(pk=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('post', post_id=post.id)
    context = {'form': form, 'post': post}
    return render(request, 'blog/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    """Delete a post"""
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts')