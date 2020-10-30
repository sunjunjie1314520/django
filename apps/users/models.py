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
    name = models.CharField(verbose_name='姓名', max_length=12, null=True, blank=True, default="")
    phone = models.CharField(verbose_name='手机号', max_length=11, null=False, blank=False, unique=True, default='')
    password = models.CharField(verbose_name='明文密码', max_length=20, null=True, blank=True, default="")
    md5_password = models.CharField(verbose_name='加密密码', max_length=32, null=True, blank=True, default="")
    create_time = models.DateTimeField(verbose_name='注册时间', default=datetime.now)
    
    class Meta:
        verbose_name = '普通用户',
        verbose_name_plural = '普通用户'
    
    def __str__(self):
        return '{}, {}'.format(self.name, self.phone)
