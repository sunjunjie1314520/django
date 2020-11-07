from django.db import models
from datetime import datetime

from users.models import Users


class Info(models.Model):

    status_choices = (
        (1, '已备案'),
        (2, '已离校'),
        (3, '已返校'),
    )

    beian = models.CharField(verbose_name="备案号", max_length=100, null=True, blank=True)
    xm = models.CharField(verbose_name="姓名", max_length=100)
    xh = models.CharField(verbose_name="学号", max_length=100)
    xb = models.CharField(verbose_name="性别", max_length=100)
    xy = models.CharField(verbose_name="学院", max_length=100)
    zy = models.CharField(verbose_name="专业", max_length=100)
    nj = models.CharField(verbose_name="年级", max_length=100, default='')

    phone = models.CharField(verbose_name="联系方式", max_length=100)
    instructor = models.CharField(verbose_name="辅导员", max_length=100)
    matter = models.TextField(verbose_name="出校事由", max_length=200)

    lxsj = models.CharField(verbose_name="出校日期", max_length=100)
    cxqs = models.CharField(verbose_name="出校起始时间", max_length=100)
    cxjs = models.CharField(verbose_name="出校结束时间", max_length=100)

    xingdong = models.CharField(verbose_name="出校行动轨迹", max_length=100)

    guiji = models.BooleanField(verbose_name="轨迹", default=True)
    fanxiao = models.BooleanField(verbose_name="返校", default=True)

    status = models.IntegerField(verbose_name="出校状态", choices=status_choices, default=1)

    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    users = models.ForeignKey(verbose_name='用户', to=Users, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "备案记录"
        verbose_name_plural = "备案记录"

    def __str__(self):
        return '{0}-{1}'.format(self.beian, self.xm)


class Examine(models.Model):
    name = models.CharField(verbose_name="审核人姓名", max_length=100)
    opinion = models.CharField(verbose_name="审核意见", max_length=100)
    info = models.ForeignKey(verbose_name='备案', to='Info', on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = "审核记录"
        verbose_name_plural = "审核记录"
        ordering = ['-id']

    def __str__(self):
        return self.name
