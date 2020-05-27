from django import forms

from .models import Category, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
