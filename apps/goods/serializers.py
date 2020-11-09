from rest_framework import serializers

from . import models


class GoodsImageSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.GoodsImage
        fields = '__all__'
        # exclude = ['goods']


class GoodsListSerializer(serializers.ModelSerializer):
    images = GoodsImageSerializer(many=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.Goods
        fields = '__all__'
