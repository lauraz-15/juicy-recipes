from django.contrib import admin
from .models import UserRecipe

# Register your models here.

# @admin.register(UserRecipe)
# class AddRecipeAdmin(admin.ModelAdmin):

#     list_display = ('name', 'recipe_title', 'posted_status', 'created')
#     search_fields = ['name', 'ingridients_list']
#     list_filter = ('posted_status', 'created')
#     prepopulated_fields = {'recipe_title': ('name',)}

