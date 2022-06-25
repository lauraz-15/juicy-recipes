from .models import Comment, Recipe
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model=Recipe
        fields=('title', 'featured_image', 'ingridients', 'content', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'ingridients': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'logged', 'type':'hidden'}),
        }
        labels = {
            'title': 'Enter the title of your recipe',
            'featured_image': 'Select a photo',
            'ingridients': 'List the ingridients here',
            'content': 'Enter directions how to make this recipe and any extra information you would like to add',
        }
       
