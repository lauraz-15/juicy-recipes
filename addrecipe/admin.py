from django.contrib import admin
from .models import UserRecipe

@admin.register(UserRecipe)
class UserRecipeAdmin(admin.ModelAdmin):

    list_display = ('name', 'recipe_slug', 'posted_status', 'created')
    search_fields = ['name', 'ingridients_list']
    list_filter = ('posted_status', 'created')
    prepopulated_fields = {'recipe_slug': ('name',)}

