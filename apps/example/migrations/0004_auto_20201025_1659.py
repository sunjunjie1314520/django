# Generated by Django 3.1.1 on 2020-10-25 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_user_gander'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gander',
            new_name='gender',
        ),
    ]