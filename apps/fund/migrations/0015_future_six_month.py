# Generated by Django 3.1.1 on 2021-03-17 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0014_future_today'),
    ]

    operations = [
        migrations.AddField(
            model_name='future',
            name='six_month',
            field=models.FloatField(default=0, verbose_name='近六月'),
        ),
    ]