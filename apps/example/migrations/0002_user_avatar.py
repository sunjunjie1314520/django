# Generated by Django 3.1.1 on 2020-11-04 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(default=None, max_length=100, verbose_name='头像'),
        ),
    ]
