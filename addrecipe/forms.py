from django import forms
from .models import UserRecipe


class UserRecipeForm(forms.ModelForm):
    class Meta:
        model=UserRecipe
        fields=('name', 'image', 'ingridients_list', 'directions',)