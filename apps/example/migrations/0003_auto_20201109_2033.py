# Generated by Django 3.1.1 on 2020-11-09 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '视频评论', 'verbose_name_plural': '视频评论'},
        ),
        migrations.AlterModelOptions(
            name='commentfavorrecord',
            options={'verbose_name': '评论点赞', 'verbose_name_plural': '评论点赞'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '视频列表', 'verbose_name_plural': '视频列表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '测试用户', 'verbose_name_plural': '测试用户'},
        ),
    ]
