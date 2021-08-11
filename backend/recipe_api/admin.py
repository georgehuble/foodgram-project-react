from django.contrib import admin

from .models import Ingredient, IngredientInRecipe, Recipe, Tag


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('name', 'author', 'id', 'followers')
    search_fields = ('name', 'author', 'teg')

    @admin.display(empty_value=None)
    def followers(self, obj):
        return obj.favourites.all().count()


@admin.register(Tag)
class AdminTeg(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)


@admin.register(IngredientInRecipe)
class AdminIngredientInRecipe(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')
    search_fields = ('recipe',)


admin.site.site_title = 'Foodgram'
admin.site.site_header = 'Foodgram'
