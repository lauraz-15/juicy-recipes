from django.contrib import admin
from .models import Recipe, Comment, Recepte
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    summernote_fields = ('content' 'ingridients')

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingridients')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Recepte)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingridients_list', 'image', 'published', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name','ingridients_list')

