# Generated by Django 3.1.1 on 2020-10-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-id'], 'verbose_name': ('用户',), 'verbose_name_plural': '用户'},
        ),
    ]