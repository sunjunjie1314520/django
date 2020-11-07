from django.contrib import admin

from .models import UserProfile, Users, UsersData


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'modify_time')
    list_display_links = ['username']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'create_time')
    list_display_links = ['phone']


@admin.register(UsersData)
class UsersDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'name', 'number', 'gender', 'college', 'major', 'grade', 'head_img', 'reviewer_name', 'create_time')
    list_display_links = ['users']
