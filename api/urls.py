from . import views
from django.urls import path

urlpatterns = [
    path("search/", views.Search.as_view(), name="search"),
    path("categories/", views.Categories.as_view(), name="categories"),
] 