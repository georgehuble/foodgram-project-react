from django.contrib import admin

from .models import CustomUser, Subscribe


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ('email', 'username', 'id')


@admin.register(Subscribe)
class AdminFollow(admin.ModelAdmin):
    list_display = ('author', 'user')
