from django.contrib import admin

from .models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'money', 'not_money', 'create_time')
    list_display_links = ['id']
