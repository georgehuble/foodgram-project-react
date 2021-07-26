from django.contrib import admin

from follow_api.models import Favourite

from follow_api.models import Subscribe


@admin.register(Favourite)
class AdminFavourite(admin.ModelAdmin):
    list_display = ('name', 'user', 'id')
    readonly_fields = ('id',)
    list_filter = ('user',)


@admin.register(Subscribe)
class AdminFollow(admin.ModelAdmin):
    list_display = ('author', 'user')
