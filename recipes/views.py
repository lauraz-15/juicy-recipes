from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe
from django.contrib.auth.models import User
from .forms import CommentForm, RecipeForm
from django.urls import reverse_lazy


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('my_recipes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Recipe deleted')
        return super(DeleteView, self).form_valid(form)


class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'update_recipe.html'
    fields = ('title', 'featured_image', 'ingridients', 'content')
    success_url = reverse_lazy('my_recipes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Recipe updated successfully')
        return super(UpdateRecipeView, self).form_valid(form)


def new_recipe(request):
    form=RecipeForm
    if request.method=='POST':
        recipeForm=RecipeForm(request.POST, request.FILES)
        if recipeForm.is_valid():
            recipeForm.save()
            messages.success(request, 'Recipe has been posted')
    return render(request, 'new.html', {'form': form})

def my_recipe_list(request):
    new = Recipe.objects.filter(author=request.user)
    return render(
        request,
        'my_recipes.html',
        {'new': new}
    )


def favorite_add(request):
    new = Recipe.objects.filter(likes=request.user)
    return render(
        request,
        'my_favorites.html',
        {'new': new}
    )

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class RecipeDetail(View):


    def get(self, request, pk, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe =  Recipe.objects.get(id=pk)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = Recipe.objects.get(id=pk)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):
    
    def post(self, request, pk, *args, **kwargs):
        recipe = Recipe.objects.get(id=pk)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[pk]))