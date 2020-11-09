from django.contrib import admin

from .models import User, News, Comment, CommentFavorRecord

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'create_time')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'user', 'content', 'create_time')

@admin.register(CommentFavorRecord)
class CommentFavorRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'user')
