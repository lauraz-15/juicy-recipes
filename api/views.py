from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View

class Categories(generic.ListView):
    template_name = "categories.html"
    paginate_by = 6

def search(request):
    """
    Renders search API recipes page
    """
    return render(request, 'search.html')


def categories(request):
    """
    Renders Inspiration page with multiple API requests/categories
    """
    return render(request, 'categories.html')
