# Generated by Django 3.1.1 on 2021-03-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0017_auto_20210318_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundall',
            name='top',
        ),
        migrations.AlterField(
            model_name='fundall',
            name='status',
            field=models.BooleanField(default=True, verbose_name='是否开启'),
        ),
    ]
