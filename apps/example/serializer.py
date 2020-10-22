

from rest_framework import serializers
from . import models

class BookModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = models.User
        fields = '__all__'