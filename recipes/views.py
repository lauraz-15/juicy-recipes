from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Recepte
from django.contrib.auth.models import User
from .forms import CommentForm, RecipeForm, RecepteForm
from django.db.models import Q

class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'recipes/update_recipe.html'
    fields = ('title', 'featured_image', 'ingridients', 'content', 'author')

    def get_success_url(self):
        return reverse('home')



class ListReceptes(ListView):
    template_name = "recipes/user_recipes.html"
    model = Recepte
    success_url = "/user_recipes/"
    context_object_name = 'receptes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        users = User.objects.filter(username=query)
        if query:
            receptes = self.model.objects.filter(
                Q(name__icontains=query) |
                Q(directions__icontains=query) |
                Q(user__in=users)
            )
        else: 
            receptes = Recepte.objects.order_by('-created_at')
        return receptes
    # receptes = Recepte.objects.filter(published=True).order_by("-created_at")

    # context = {
    #     'receptes': receptes
    # }

    # return render(request, 'recipes/user_recipes.html', context)



def addRecepte(request):
    form = RecepteForm()

    if request.method == 'POST':
        form = RecepteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('recipes/add_recepte')
    else:
        form = RecepteForm()

    context = {
        "form":form
    }

    return render(request, 'recipes/add_recepte.html', context)



def new_recipe(request):
    form=RecipeForm
    if request.method=='POST':
        recipeForm=RecipeForm(request.POST, request.FILES)
        if recipeForm.is_valid():
            recipeForm.save()
            messages.success(request,'Recipe has been saved')
            # return redirect('recipes/new')
    return render(request, 'recipes/new.html', {'form': form})


def my_recipe_list(request):
    new = Recipe.objects.filter(author=request.user)
    return render(
        request,
        'recipes/my_recipes.html',
        {'new': new}
    )


def favorite_add(request):
    new = Recipe.objects.filter(likes=request.user)
    return render(
        request,
        'recipes/my_favorites.html',
        {'new': new}
    )

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "recipes/index.html"
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
            "recipes/recipe_detail.html",
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
            "recipes/recipe_detail.html",
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