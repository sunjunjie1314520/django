# Generated by Django 3.1.1 on 2020-09-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20200927_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], default=True, max_length=6, null=True, verbose_name='性别'),
        ),
    ]
