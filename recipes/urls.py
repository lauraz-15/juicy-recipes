from . import views
from django.urls import path

urlpatterns = [
    path("recipes", views.RecipeList.as_view(), name="home"),
    path("user_recipes", views.ListReceptes.as_view(), name="user_recipes"),
    path("my_favorites/", views.favorite_add, name="my_favorites"),
    path("my_recipes/", views.my_recipe_list, name="my_recipes"),
    path('add_recepte/', views.addRecepte, name='add_recepte'),
    path("new/", views.new_recipe, name="new"),
    path('recipe_detail/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:pk>', views.RecipeLike.as_view(), name='recipe_like'),
]