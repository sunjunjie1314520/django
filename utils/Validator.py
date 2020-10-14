import re
from rest_framework.exceptions import ValidationError

def phone_validator(value):
    """
    手机号
    """
    reg = r"^(1[3|4|5|6|7|8|9])\d{9}$"
    if not re.match(reg, value):
        raise ValidationError('请正确填写11位手机号码')

def name_validator(value):
    """
    姓名
    """
    reg = r"^([\u4e00-\u9fa5]{1,10}|[a-zA-Z]{1,10})$"
    if not re.match(reg, value):
        raise ValidationError('名字仅限于中文和英文')