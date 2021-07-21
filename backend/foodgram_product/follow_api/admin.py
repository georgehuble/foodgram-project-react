from django.contrib import admin

from follow_api.models import Favorite


@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('recipe', 'user')
