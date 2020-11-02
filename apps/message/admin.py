from django.contrib import admin

from .models import Message, Visit


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'textarea', 'create_time')
    list_display_links = ['id', 'name']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'create_time')
    list_display_links = ['address']
