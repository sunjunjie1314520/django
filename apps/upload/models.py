from django.db import models

from utils import time_handle, file_handle

def directory_path(instance, filename):
    return "upload/img/%s/%s%s" % (time_handle.currentDate(), time_handle.timeStamp(), file_handle.extension(filename))


class Image(models.Model):
    """
    上传图片
    """
    img = models.ImageField(verbose_name='文件名称', upload_to=directory_path)
    create_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        verbose_name = '图片表',
        verbose_name_plural = '图片表'

    def __str__(self):
        return self.img
