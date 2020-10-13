import re
from rest_framework.exceptions import ValidationError

def phone_validator(value):
    """
    手机号正则
    """
    reg = r"^(1[3|4|5|6|7|8|9])\d{9}$"
    if not re.match(reg, value):
        raise ValidationError('手机号格式错误')
