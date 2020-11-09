# Generated by Django 3.1.1 on 2020-11-08 22:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AddField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255, verbose_name='图片地址')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
            },
        ),
    ]