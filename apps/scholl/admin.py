
from django.contrib import admin

from .models import Info, Examine, Record


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'beian', 'users', 'xm', 'xb', 'xh', 'xy', 'zy', 'nj', 'status', 'fanxiao', 'lxsj', 'fxrq', 'create_time')
    list_display_links = ['beian']

@admin.register(Examine)
class ExamineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'opinion', 'info', 'create_time')
    list_display_links = ['name']

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'money', 'create_time')
    list_display_links = ['users']
