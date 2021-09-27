from django_filters import rest_framework as filters

from .models import Ingredient, Recipe


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IngridientFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='gt')

    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags__slug', lookup_expr='in')
    author = CharFilterInFilter(field_name='author', lookup_expr='in')
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    is_favorited = CharFilterInFilter(field_name='is_favorited',
                                      lookup_expr='in')
    is_in_shopping_cart = CharFilterInFilter(field_name='is_in_shopping_cart',
                                             lookup_expr='in')

    class Meta:
        model = Recipe
        fields = []
