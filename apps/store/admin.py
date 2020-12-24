from django.contrib import admin

from .models import Code, Type


@admin.register(Type)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'update_time', 'create_time')
    list_display_links = ['name']


@admin.register(Code)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'update_time', 'create_time')
    list_display_links = ['name']
