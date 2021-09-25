from django_filters import rest_framework as filters

from .models import Ingredient, Tag


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IngridientFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='gt')

    class Meta:
        model = Ingredient
        fields = ['name']


class TagFilter(filters.FilterSet):
    id = CharFilterInFilter(field_name='id', lookup_expr='gt')

    class Meta:
        model = Tag
        fields = ['id']
