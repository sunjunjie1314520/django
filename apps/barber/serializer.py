

from rest_framework import serializers

from . import models

class PostSerializer(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(format='%H:%M:%S', read_only=True) # %Y-%m-%d %H:%M:%S

    curr_date = serializers.CharField(error_messages={
        'required': '时间必选',
        'blank': '请先选择时间',
    })
    price = serializers.CharField(error_messages={
        'required': '价格必填',
        'blank': '请输入价格',
    })
    remarks = serializers.CharField(error_messages={
        'required': '备注必填',
        'blank': '请输入备注',
    })

    # def validate(self, attrs):
    #     del attrs['create_time']
    #     return attrs
    class Meta:
        model = models.Bill
        fields = "__all__"

