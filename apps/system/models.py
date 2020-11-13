from django.db import models
from datetime import datetime

class Config(models.Model):
    """
    配置表
    """
    money = models.PositiveIntegerField(verbose_name='当日返校价格', default=0)
    not_money = models.PositiveIntegerField(verbose_name='非当日返校价格', default=0)
    create_time = models.DateTimeField(verbose_name='注册时间', default=datetime.now)

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.money
