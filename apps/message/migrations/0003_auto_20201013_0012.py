# Generated by Django 3.1.1 on 2020-10-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20201012_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='手机号'),
        ),
    ]
