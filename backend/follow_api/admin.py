from django.contrib import admin

from recipe_api.models import Shopping

from .models import Favourite, Subscribe


@admin.register(Favourite)
class AdminFavourite(admin.ModelAdmin):
    list_display = ('name', 'user', 'id')
    readonly_fields = ('id',)
    list_filter = ('user',)


@admin.register(Subscribe)
class AdminFollow(admin.ModelAdmin):
    list_display = ('author', 'user')


@admin.register(Shopping)
class AdminShopping(admin.ModelAdmin):
    list_display = ('name', 'user', 'id')
    readonly_fields = ('id',)
    list_filter = ('user',)
