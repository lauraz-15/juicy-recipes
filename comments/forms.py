from .models import Comment, Recipe
from django import forms
from django.forms import Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=('title', 'slug', 'featured_image', 'ingridients', 'content', 'author', 'status')
        widgets = {
            'ingridients': Textarea()
        }
        # prepopulated_fields = {'slug': ('title',)}    
