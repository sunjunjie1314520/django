import re
from rest_framework.exceptions import ValidationError

def phone_validator(value):
    """
    手机号
    """
    reg = r"^(1[3|4|5|6|7|8|9])\d{9}$"
    if not re.match(reg, value):
        raise ValidationError('请正确填写11位手机号码')

def money_validator(value):
    """
    余额
    """
    if not value.isdecimal():
        raise ValidationError('金额只能为数字')
    if float(value) < 1:
        raise ValidationError('金额不能小于1')

def name_validator(value):
    """
    姓名
    """
    reg = r"^([\u4e00-\u9fa5]{1,10}|[a-zA-Z]{1,10})$"
    if not re.match(reg, value):
        raise ValidationError('名字仅限于中文和英文')

def url_validator(value):
    """
    URL地址
    """
    reg = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    if not re.match(reg, value):
        raise ValidationError('URL地址格式不正确')

