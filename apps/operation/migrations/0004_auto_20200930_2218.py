# Generated by Django 3.1.1 on 2020-09-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20200927_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], default='男', max_length=6, null=True, verbose_name='性别'),
        ),
    ]