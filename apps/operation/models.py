from django.db import models

class Address(models.Model):
    """
    收货地址
    """
    GENDER = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.CharField(max_length=10, verbose_name='收货人')
    gender = models.CharField(max_length=6, null=True, blank=True, default="男", choices=GENDER, verbose_name='性别')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=10, verbose_name='详细地址')
    house = models.CharField(max_length=10, verbose_name='门牌号')
    label = models.CharField(max_length=10, null=True, verbose_name='标签')

    class Meta:
        verbose_name ="收货地址"
        verbose_name_plural = "收货地址"
    
    def __str__(self):
        return self.name