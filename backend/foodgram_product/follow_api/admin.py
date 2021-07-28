from django.contrib import admin

from .models import Favourite

from .models import Subscribe

from .models import Shopping


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
