from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View



class Search(generic.ListView):
    template_name = "search.html"
    paginate_by = 6

class Categories(generic.ListView):
    template_name = "categories.html"
    paginate_by = 6
