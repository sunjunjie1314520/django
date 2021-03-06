# Generated by Django 3.1.1 on 2020-11-06 00:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='审核人姓名')),
                ('opinion', models.CharField(max_length=100, verbose_name='审核意见')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '审核记录',
                'verbose_name_plural': '审核记录',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beian', models.CharField(blank=True, default='', max_length=100, verbose_name='备案号')),
                ('xm', models.CharField(blank=True, max_length=100, verbose_name='姓名')),
                ('xh', models.CharField(blank=True, max_length=100, verbose_name='学号')),
                ('xb', models.CharField(blank=True, max_length=100, verbose_name='性别')),
                ('xy', models.CharField(blank=True, max_length=100, verbose_name='学院')),
                ('zy', models.CharField(blank=True, max_length=100, verbose_name='专业')),
                ('nj', models.CharField(blank=True, max_length=100, verbose_name='年级')),
                ('phone', models.CharField(blank=True, max_length=100, verbose_name='联系方式')),
                ('instructor', models.CharField(blank=True, max_length=100, verbose_name='辅导员')),
                ('matter', models.TextField(blank=True, max_length=200, verbose_name='出校事由')),
                ('lxsj', models.CharField(blank=True, max_length=100, verbose_name='出校日期')),
                ('cxqs', models.CharField(blank=True, max_length=100, verbose_name='出校起始时间')),
                ('cxjs', models.CharField(blank=True, max_length=100, verbose_name='出校结束时间')),
                ('guiji', models.BooleanField(blank=True, null=True, verbose_name='轨迹')),
                ('fanxiao', models.BooleanField(blank=True, null=True, verbose_name='返校')),
                ('xingdong', models.CharField(blank=True, max_length=100, verbose_name='出校行动轨迹')),
                ('status', models.IntegerField(choices=[(1, '已备案'), (2, '已离校'), (3, '已返校')], default=1, verbose_name='出校状态')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '备案记录',
                'verbose_name_plural': '备案记录',
                'ordering': ['-id'],
            },
        ),
    ]
