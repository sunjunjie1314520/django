from rest_framework import serializers
from . import models
from django.forms.models import model_to_dict


class BookModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(label='添加时间', format='%Y-%m-%d %H:%M:%S', required=False)
    sex = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {'gender': {'write_only': True}}
        # exclude = ['gender', ]


class NewsModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    comment = serializers.SerializerMethodField()

    def get_comment(self, obj):
        first_queryset = models.Comment.objects.filter(news=obj, depth=1)

        first_json = [{
            'id': row.id,
            'content': row.content,
            'create_time': row.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'favor_count': row.favor_count,
            'user': {
                'id': row.user.id,
                'name': row.user.name,
                'avatar': row.user.avatar,
            },
            'child': []

        } for row in first_queryset]

        first_id_list = [row.id for row in first_queryset]

        # 'id',
        # 'content',
        # 'create_time',
        # 'favor_count',
        # 'user__name',
        # 'user__avatar',
        # 'reply_id',
        # 'reply__user__avatar',
        # 'reply__user__name'

        secound_queryset = models.Comment.objects.filter(news=obj, depth=2, reply_id__in=first_id_list)

        secound_json = [{
            'id': row.id,
            'content': row.content,
            'create_time': row.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'favor_count': row.favor_count,
            'user': {
                'id': row.user.id,
                'name': row.user.name,
                'avatar': row.user.avatar,
            },
            'reply_id': row.reply.id,
            'reply_user': {
                'name': row.reply.user.name,
                'avatar': row.reply.user.avatar,
            },

        } for row in secound_queryset]

        import collections
        first_dict = collections.OrderedDict()
        for item in first_json:
            first_dict[item['id']] = item

        for node in secound_json:
            first_dict[node['reply_id']]['child'].append(node)

        print(first_dict)

        return first_json

    class Meta:
        model = models.News
        fields = '__all__'
