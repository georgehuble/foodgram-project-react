from django_filters import rest_framework as filters

from .models import Ingredient


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class IngridientFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Ingredient
        fields = ['name']
