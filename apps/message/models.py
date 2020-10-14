from django.db import models

from datetime import datetime

class Message(models.Model):
    """
    留言表
    """
    name = models.CharField( verbose_name="姓名", max_length=10)
    phone = models.CharField(verbose_name="手机号", max_length=11, unique=True)
    textarea = models.CharField(verbose_name="留言内容", max_length=100)
    create_time = models.DateTimeField(verbose_name="留言时间", default=datetime.now, null=True, blank=True)

    class Meta:
        verbose_name ="留言内容"
        verbose_name_plural = "留言内容"
    
    def __str__(self):
        return self.name