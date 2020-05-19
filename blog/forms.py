from django import forms

from .models import Category, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
        labels = {'title': 'Title', 'content': '', 'category': 'Category'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        labels = {'title': 'Title'}