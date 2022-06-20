from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class UserRecipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    recipe_slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    ingridients_list = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    posted_status = models.IntegerField(choices=STATUS, default=0)
    favorites = models.ManyToManyField(
        User, related_name='favorites', blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name

    def number_of_favorites(self):
        return self.favorites.count()

