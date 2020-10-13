from django.db import models

class UserInfo(models.Model):
    """
    用户表
    """
    phone = models.CharField(max_length=11, verbose_name="手机号")
    

class Goods(models.Model):
    """
    商品表
    """
    title = models.CharField(max_length=100, verbose_name="商品名称")
    price = models.PositiveIntegerField(verbose_name="价格")

class Order(models.Model):
    """
    订单表
    """
    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
        (3, "待发货"),
        (4, "已完成"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices)
    goods = models.ForeignKey(to='Goods', on_delete=models.CASCADE, verbose_name="商品")
    user = models.ForeignKey(to="UserInfo", on_delete=models.CASCADE, verbose_name="用户")
    number = models.CharField(max_length=32, verbose_name="订单号")

