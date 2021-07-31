from django.contrib import admin

from .models import Ingredient, Recipe, Tag


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ('name', 'amount', 'measurement_unit')
    search_fields = ('name',)


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('name', 'author', 'text', 'id')
    search_fields = ('name',)


@admin.register(Tag)
class AdminTeg(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)


admin.site.site_title = 'Foodgram'
admin.site.site_header = 'Foodgram'