from django_filters import rest_framework as filters

from .models import Ingredient


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IngridientFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='gt')

    class Meta:
        model = Ingredient
        fields = ['name']
