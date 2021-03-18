from django.db import models


class Profit(models.Model):
    money = models.FloatField(default=0, verbose_name='买入金额')
    name = models.CharField(max_length=30, verbose_name='基金名称')
    code = models.CharField(max_length=30, null=True, verbose_name='基金代号')
    sum = models.FloatField(default=0, verbose_name='累计收益')
    phone = models.CharField(max_length=256, null=True, verbose_name='手机号')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = "基金配置"
        verbose_name_plural = "基金配置"

    def __str__(self):
        return f'{self.code}-{self.phone}'


class FundAll(models.Model):
    code = models.CharField(max_length=30, null=True, verbose_name='代号')
    name = models.CharField(max_length=30, verbose_name='名称')
    type = models.CharField(max_length=10, verbose_name='类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='是否打开')
    top = models.BooleanField(default=False, verbose_name='是否置顶')

    class Meta:
        verbose_name = "所有基金"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.code}-{self.name}'


class Future(models.Model):
    code = models.ForeignKey(to=FundAll, on_delete=models.CASCADE, verbose_name='代号')
    today = models.FloatField(verbose_name="今日估值", default=0)
    day = models.FloatField(verbose_name="日涨幅", default=0)
    week = models.FloatField(verbose_name="近一周", default=0)
    one_month = models.FloatField(verbose_name="近一月", default=0)
    three_month = models.FloatField(verbose_name="近三月", default=0)
    six_month = models.FloatField(verbose_name="近六月", default=0)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = "数据排行"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.code.code}-{self.code.name}'


class User(models.Model):
    user = models.CharField(max_length=10, verbose_name='姓名', null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = "基金用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user}'


class Collection(models.Model):
    user = models.ForeignKey(to=User, verbose_name='用户', blank=True, on_delete=models.CASCADE)
    fund = models.ForeignKey(to=Future, verbose_name='基金', blank=True, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = "基金用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user.name}'
