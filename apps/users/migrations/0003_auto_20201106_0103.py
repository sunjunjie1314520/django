# Generated by Django 3.1.1 on 2020-11-06 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usersdata_reviewer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersdata',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.users', verbose_name='用户'),
        ),
    ]