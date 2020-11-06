from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class UserProfile(AbstractUser):
    """
    超级用户
    """
    modify_time = models.DateTimeField(verbose_name='最后修改时间', auto_now=True)

    class Meta:
        verbose_name = '管理员',
        verbose_name_plural = '管理员'
    
    def __str__(self):
        return self.username


class Users(models.Model):
    """
    普通用户
    """
    phone = models.CharField(verbose_name='手机号', max_length=11, null=False, blank=False, unique=True, default='')
    create_time = models.DateTimeField(verbose_name='注册时间', default=datetime.now)

    class Meta:
        verbose_name = '普通用户',
        verbose_name_plural = '普通用户'
    
    def __str__(self):
        return self.phone


class UsersData(models.Model):
    """
    用户资料
    """
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男')
    )
    users = models.ForeignKey(verbose_name='用户', to='Users', on_delete=models.CASCADE, null=True, blank=True)
    money = models.FloatField(verbose_name='余额', default=0)
    name = models.CharField(verbose_name='姓名', max_length=30, default='')
    number = models.CharField(verbose_name='学号', max_length=30, default='')
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_CHOICES, default=1)
    college = models.CharField(verbose_name='学院', max_length=30, default='天津师范大学')
    major = models.CharField(verbose_name='专业', max_length=30, default='')
    grade = models.CharField(verbose_name='年级', max_length=30, default='2020')
    head_img = models.CharField(verbose_name='头像', max_length=255, null=True, blank=True, default='')
    reviewer_name = models.CharField(verbose_name='审核人姓名', max_length=30, default='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '用户资料',
        verbose_name_plural = '用户资料'

    def __str__(self):
        return self.users.phone
