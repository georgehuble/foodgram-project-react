from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ('email', 'username', 'id')
    search_fields = ('email', 'username')
