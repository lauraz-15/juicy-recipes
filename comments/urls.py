from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("search/", views.Search.as_view(), name="search"),
    path("categories/", views.Categories.as_view(), name="categories"),
    path("my_favorites/", views.favorite_add, name="my_favorites"),
    path("new/", views.new_recipe, name="new"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
]
