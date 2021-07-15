from django.contrib import admin

from .models import Ingredient, Recipe, Teg, CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ('title', 'amount', 'dimension')
    search_fields = ('title',)


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('name', 'author', 'discription')
    search_fields = ('title',)


@admin.register(Teg)
class AdminTeg(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)


admin.site.site_title = 'Foodgram'
admin.site.site_header = 'Foodgram'
