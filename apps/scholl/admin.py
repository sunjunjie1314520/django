
from django.contrib import admin

from .models import Info, Examine


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'beian', 'xm', 'xb', 'xh', 'xy', 'zy', 'nj', 'status', 'users', 'create_time')
    list_display_links = ['beian']

@admin.register(Examine)
class ExamineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'opinion', 'info', 'create_time')
    list_display_links = ['name']