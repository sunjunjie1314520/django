from django.db import models
from datetime import datetime

class Bill(models.Model):
    """
    流水表
    """
    curr_date = models.CharField(verbose_name="日期", max_length=20)
    price = models.CharField(verbose_name="价格", max_length=20)
    remarks = models.CharField(verbose_name="备注", max_length=20)
    create_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name ="流水"
        verbose_name_plural = "流水"
    
    def __str__(self):
        return self.price
