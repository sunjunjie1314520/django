# Generated by Django 3.1.1 on 2020-10-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
    ]