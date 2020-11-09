from django.db import models
from datetime import datetime


class User(models.Model):
    """
    用户表
    """
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男'),
    )
    name = models.CharField(verbose_name='姓名', max_length=30)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_CHOICES, default=1)
    avatar = models.CharField(verbose_name='头像', max_length=100, default=None)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = "测试用户"
        verbose_name_plural = "测试用户"

    def __str__(self):
        return self.name


class News(models.Model):
    """
    动态表
    """
    title = models.CharField(verbose_name='标题', max_length=30)
    content = models.TextField(verbose_name='内容', max_length=100)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        verbose_name = "视频列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Comment(models.Model):
    """
    评论表记录
    """
    news = models.ForeignKey(verbose_name='动态', to='News', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='用户', to='User', on_delete=models.CASCADE)

    content = models.CharField(verbose_name='评论内容', max_length=255)
    reply = models.ForeignKey(verbose_name='回复', to='self', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='replys')
    depth = models.IntegerField(verbose_name='评论层级', null=True, blank=True, default=1)
    root = models.ForeignKey(verbose_name='根评论', to='self', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='roots')
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)

    class Meta:
        verbose_name = "视频评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class CommentFavorRecord(models.Model):
    """
    评论点赞
    """
    comment = models.ForeignKey(verbose_name='动态', to='Comment', on_delete=models.CASCADE)
    user = models.ForeignKey(verbose_name='用户', to='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论点赞"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment.content
