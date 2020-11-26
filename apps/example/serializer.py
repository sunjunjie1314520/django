from rest_framework import serializers
from . import models

from users.serializers import UsersSerializer


class CommentSerializer1(serializers.ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = models.Comment
        exclude = ['news', 'root', 'depth']


class CommentSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    reply = CommentSerializer1()
    favor_count = serializers.SerializerMethodField()
    is_zan = serializers.SerializerMethodField()

    @classmethod
    def get_favor_count(cls, instance):

        count = models.CommentFavorRecord.objects.filter(comment=instance).count()
        return count

    def get_is_zan(self, instance):

        user = self.context['request'].user
        if user:
            return models.CommentFavorRecord.objects.filter(comment=instance, user_id=user.id).exists()
        else:
            return False

    class Meta:
        model = models.Comment
        # fields = '__all__'
        exclude = ['news', 'root', 'depth']
        # depth = 1

################## 新闻详情动态 Serializer ##################
class NewsModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    comments = serializers.SerializerMethodField()

    def get_comments(self, instance):
        query_set = models.Comment.objects.filter(news=instance, depth=1)[:10]
        serializer = CommentSerializer(instance=query_set, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = models.News
        fields = '__all__'
