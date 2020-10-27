from django.db import models
from datetime import datetime

class User(models.Model):
    """
    用户表
    """
    GENDER_CHOICES = (
        ('F', '男'),
        ('M', '女'),
    )
    name = models.CharField(verbose_name='姓名', max_length=30)
    gender = models.CharField(verbose_name='性别', max_length=1, choices=GENDER_CHOICES, default='F')
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        ordering = ['-id']

    def __str__(self):
        return self.name
