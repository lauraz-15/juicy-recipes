from . import views
from django.urls import path

urlpatterns = [
    path("search/", views.search, name="search"),
    path("categories/", views.categories, name="categories"),
] 