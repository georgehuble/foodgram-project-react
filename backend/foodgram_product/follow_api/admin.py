from django.contrib import admin

from follow_api.models import Favourite


@admin.register(Favourite)
class AdminFavourite(admin.ModelAdmin):
    list_display = ('name', 'user', 'id')
    readonly_fields = ('id',)
