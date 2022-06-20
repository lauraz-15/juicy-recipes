from .models import Comment, Recipe
from django import forms
from django_summernote.admin import SummernoteModelAdmin

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=('title', 'slug', 'featured_image', 'ingridients', 'content', 'author', 'status')
        summernote_fields = ('content' 'ingridients')
        prepopulated_fields = {'slug': ('title',)}    
