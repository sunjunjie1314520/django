from django.db import models


class Profit(models.Model):
    money = models.FloatField(default=0, verbose_name='收益金额')
    name = models.CharField(max_length=30, verbose_name='基金名称')
    code = models.CharField(max_length=30, null=True, verbose_name='基金代号')
    sum = models.FloatField(default=0, verbose_name='累计收益')
    phone = models.CharField(max_length=11, null=True, verbose_name='手机号')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f'{self.code}-{self.phone}'
