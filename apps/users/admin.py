from django.contrib import admin

from .models import UserProfile, Users


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'modify_time')
    list_display_links = ['id', 'username']

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'password', 'md5_password', 'create_time')
    list_display_links = ['id', 'phone']
