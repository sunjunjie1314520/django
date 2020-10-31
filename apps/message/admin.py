from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'textarea', 'create_time')
    list_display_links = ['id', 'name']