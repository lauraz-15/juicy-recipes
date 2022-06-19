from . import views
from django.urls import path


urlpatterns = [
    path("add_recipes/", views.user_recipe, name="add_recipes"),
    path("my_recipes/", views.list_my_recipes, name="my_recipes"),
]