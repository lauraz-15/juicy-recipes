from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import generic, View
from .models import UserRecipe
from .forms import UserRecipeForm 

# Create your views here.
def user_recipe(request):
    form=UserRecipeForm
    if request.method=='POST':
        userRecipeForm=UserRecipeForm(request.POST)
        if userRecipeForm.is_valid():
            userRecipeForm.save()
            messages.success(request,'Recipe has been saved')
            return redirect('/add_recipe')
    return render(request, 'add_recipe.html', {'form': form})



# class List_my_recipes(generic.ListView):
#     model = UserRecipeF
#     queryset = UserRecipe.objects.filter(posted_status=1).order_by("-created")
#     template_name = "my_recipes.html"
#     paginate_by = 6


def list_my_recipes(request):
    new = UserRecipe.objects.filter(added_by_user=request.user)
    return render(
        request,
        'my_recipes.html',
        {'new': new}
    )
