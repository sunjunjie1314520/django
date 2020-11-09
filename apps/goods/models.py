from django.db import models
from datetime import datetime


class Goods(models.Model):

    title = models.CharField(verbose_name='标题', max_length=30)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GoodsImage(models.Model):

    goods = models.ForeignKey(verbose_name='商品', to=Goods, related_name='images', on_delete=models.CASCADE)
    image = models.CharField(verbose_name='图片地址', max_length=255)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.image
