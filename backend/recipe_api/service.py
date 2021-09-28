from django_filters import rest_framework as filters
from rest_framework import serializers
from .models import Ingredient, Recipe
from follow_api.models import Favourite, Shopping
from .serializers import RecipeSerializer

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IngridientFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='gt')

    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeFilter(filters.FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug',
                                           conjoined=False)
    author = CharFilterInFilter(field_name='author', lookup_expr='in')
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    is_favorited = filters.BooleanFilter(method='check_if_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(method='check_if_is_in_shopping_cart')

    class Meta:
        model = Recipe
        fields = ['tags', 'author', 'name', 'is_favorited', 'is_in_shopping_cart']

    def check_if_is_favorited(self, query, name, value):
        user = self.request.user
        if value:
            return Recipe.objects.filter(favourites__user=user)
        return Recipe.objects.all()

    def check_if_is_in_shopping_cart(self, query, name, value):
        user = self.request.user
        if value:
            return Recipe.objects.filter(shopping__user=user)
        return Recipe.objects.all()
