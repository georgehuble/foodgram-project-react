from rest_framework import generics, permissions, views, response
from rest_framework.generics import get_object_or_404

from .models import Favorite
from .serializers import FavoriteSerializer
from recipe_api.models import Recipe
from user_api.models import CustomUser


class ListFavoriteView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.recipe)


class FavoriteView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Recipe.objects.all()
        exclude_recipes = Recipe.objects.filter(
            favorite_recipes__user=self.request.user
        )
        queryset = queryset.exclude(
            id__in=exclude_recipes
        )