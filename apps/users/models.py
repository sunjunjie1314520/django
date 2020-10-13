from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=12, null=True, blank=True, default="")

    class Meta:
        verbose_name = '用户',
        verbose_name_plural = '用户'
    
    def __str__(self):
        return self.username
