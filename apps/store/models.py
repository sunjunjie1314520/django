from django.db import models


class Type(models.Model):
    """
    代码库
    """
    name = models.CharField(max_length=100, verbose_name='分类名称')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '代码分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Code(models.Model):
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE, verbose_name='分类', related_name='codes')

    name = models.CharField(max_length=100, verbose_name='实例名称', default='未取名')

    css = models.TextField(verbose_name='css', null=True, blank=True)
    javascript = models.TextField(verbose_name='javascript', null=True, blank=True)
    html = models.TextField(verbose_name='html', null=True, blank=True)
    code = models.TextField(verbose_name='code', null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '代码仓库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type.name
