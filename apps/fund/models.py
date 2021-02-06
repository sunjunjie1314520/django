from django.db import models

# Create your models here.


class Profit(models.Model):
    money = models.FloatField(default=0, verbose_name='收益金额')
    name = models.CharField(max_length=30, verbose_name='基金名称')
    sum = models.FloatField(default=0, verbose_name='累计收益')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
