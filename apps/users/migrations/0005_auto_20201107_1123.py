# Generated by Django 3.1.1 on 2020-11-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201106_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdata',
            name='grade',
            field=models.CharField(default='', max_length=30, verbose_name='年级'),
        ),
    ]
