from django.contrib import admin

from .models import UserProfile, Users, UsersData


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'date_joined', 'modify_time')
    list_display_links = ['id', 'username']


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'password', 'md5_password', 'create_time')
    list_display_links = ['id', 'phone']

@admin.register(UsersData)
class UsersDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'money', 'name', 'number', 'gender', 'college', 'major', 'grade', 'head_img', 'reviewer_name', 'create_time')
    list_display_links = ['id']
