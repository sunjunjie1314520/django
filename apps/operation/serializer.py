

from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(error_messages={
        'required': '姓名为必填项',
        'blank': '姓名不能为空',
    })
    house = serializers.CharField(min_length=5, max_length=10, label='门牌号', error_messages={
        'required': '门牌号为必填项',
        'blank': '门牌号不能为空',
        'min_length': '门牌号不能少于5个文字',
        'max_length': '门牌号不能大于10个文字',
    })
    class Meta:
        model = Address
        fields = '__all__'
