# Generated by Django 3.1.1 on 2020-11-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201107_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdata',
            name='grade',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='年级'),
        ),
        migrations.AlterField(
            model_name='usersdata',
            name='head_img',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='头像'),
        ),
    ]
