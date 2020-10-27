from rest_framework import serializers
from . import models


class BookModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='添加时间', format='%Y-%m-%d %H:%M:%S', required=False)
    sex = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {'gender': {'write_only': True}}
        # exclude = ['gender', ]