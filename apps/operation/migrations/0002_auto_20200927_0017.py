# Generated by Django 3.1.1 on 2020-09-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='gender',
            field=models.CharField(blank=True, choices=[(0, '女'), (1, '男')], default=0, max_length=6, null=True, verbose_name='性别'),
        ),
    ]