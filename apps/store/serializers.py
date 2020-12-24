
from rest_framework import serializers

from . import models


class CodeSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.Code
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    codes = CodeSerializer(many=True)

    class Meta:
        model = models.Type
        fields = '__all__'
