from . import views
from django.urls import path
from .views import UpdateRecipeView, ListView, DeleteRecipeView

urlpatterns = [
    path("my_favorites/", views.favorite_add, name="my_favorites"),
    path("my_recipes/", views.my_recipe_list, name="my_recipes"),
    path("new/", views.new_recipe, name="new"),
    path('update_recipe/<int:pk>', views.UpdateRecipeView.as_view(), name='update_recipe'),
    path('delete_recipe/<int:pk>/delete', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('recipe_detail/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:pk>', views.RecipeLike.as_view(), name='recipe_like'),
]