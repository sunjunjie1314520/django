from django.contrib import admin

from .models import Profit


@admin.register(Profit)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'phone', 'money', 'sum', 'create_time')
    list_display_links = ['name']
