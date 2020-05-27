from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .models import Post, Category
from .forms import PostForm, CategoryForm
from .utils import ObjectCreateMixin


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    """Show all blog posts"""
    context = {'post_list': Post.objects.all()}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, year, month, slug):
    """Detail view for a post"""
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug__iexact=slug
    )
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


class PostCreate(ObjectCreateMixin, View):

    form_class = PostForm
    template_name = "blog/post_form.html"


class PostUpdate(View):

    form_class = PostForm
    model = Post
    template_name = "blog/post_form_update.html"

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        form = self.form_class(instance=post)
        context = {'form': form, 'post': post}
        return render(request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form': bound_form, 'post': post}
            return render(request, self.template_name, context)

    def get_object(self, year, month, slug):
        return get_object_or_404(
            self.model,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug
        )


class PostDelete(View):

    model = Post
    template_name = "blog/post_confirm_delete.html"

    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        return render(request, self.template_name, {'post': post})

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        post.delete()
        return redirect('post_list')

    def get_object(self, year, month, slug):
        return get_object_or_404(
            self.model,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug
        )


def category_list(request):
    """Show all categories"""
    context = {'category_list': Category.objects.all()}
    return render(request, 'blog/category_list.html', context)


def category_detail(request, slug):
    category = get_object_or_404(
        Category,
        slug__iexact=slug
    )
    context = {'category': category}
    return render(request, 'blog/category_detail.html', context)


class CategoryCreate(ObjectCreateMixin, View):

    form_class = CategoryForm
    template_name = "blog/category_form.html"


class CategoryUpdate(View):

    form_class = CategoryForm
    model = Category
    template_name = "blog/category_form_update.html"

    def get(self, request, slug):
        category = self.get_object(slug)
        form = self.form_class(instance=category)
        context = {'form': form, 'category': category}
        return render(request, self.template_name, context)

    def post(self, request, slug):
        category = self.get_object(slug)
        bound_form = self.form_class(request.POST, instance=category)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        else:
            context = {'form': bound_form, 'category': category}
            return render(request, self.template_name, context)

    def get_object(self, slug):
        return get_object_or_404(
            self.model,
            slug__iexact=slug
        )


class CategoryDelete(View):

    model = Category
    template_name = "blog/category_confirm_delete.html"

    def get(self, request, slug):
        category = self.get_object(slug)
        return render(request, self.template_name, {'category': category})

    def post(self, request, slug):
        cateogry = self.get_object(slug)
        cateogry.delete()
        return redirect('category_list')

    def get_object(self, slug):
        return get_object_or_404(
            self.model,
            slug__iexact=slug
        )
