
from rest_framework import serializers

from . import models


class UsersSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='添加时间', format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = models.Users
        fields = '__all__'
        extra_kwargs = {'gender': {'write_only': True}}
