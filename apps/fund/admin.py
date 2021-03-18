from django.contrib import admin

from .models import Profit, User


@admin.register(Profit)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'phone', 'money', 'sum', 'create_time')
    list_display_links = ['name']


@admin.register(User)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'create_time')
    list_display_links = ['user']
