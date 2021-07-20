from django.contrib import admin

from .models import Ingredient, Recipe, Tag, Favorite, Shopping


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ('name', 'amount', 'measurement_unit')
    search_fields = ('name',)


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('name', 'author', 'text')
    search_fields = ('name',)


@admin.register(Tag)
class AdminTeg(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)


@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('author', 'name')


@admin.register(Shopping)
class AdminShopping(admin.ModelAdmin):
    pass


admin.site.site_title = 'Foodgram'
admin.site.site_header = 'Foodgram'
