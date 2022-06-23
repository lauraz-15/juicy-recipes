from .models import Comment, Recipe, Recepte
from django import forms


class RecepteForm(forms.ModelForm):
    class Meta:
        model = Recepte
        fields = ['name', 'ingridients_list', 'directions', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'ingridients_list': forms.Textarea(attrs={'class': 'form-control'}),
            'directions': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Enter the title of your recipe:',
            'image': 'Select a photo: ',
            'ingridients_list': 'List the ingridients here: ',
            'directions': 'Enter directions how to make this recipe and any extra comments information you would like to add: ',
        }



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
        }
        labels = {
            'title': 'Enter the title of your recipe',
            'featured_image': 'Select a photo',
            'ingridients': 'List the ingridients here',
            'content': 'Enter directions how to make this recipe and any extra information you would like to add',
        }
       
