# Generated by Django 3.1.1 on 2020-11-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholl', '0005_auto_20201106_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='matter',
            field=models.TextField(max_length=200, verbose_name='出校事由'),
        ),
    ]