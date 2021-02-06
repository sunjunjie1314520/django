# Generated by Django 3.1.1 on 2020-12-23 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '代码分类',
                'verbose_name_plural': '代码分类',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css', models.TextField(blank=True, null=True, verbose_name='css')),
                ('javascript', models.TextField(blank=True, null=True, verbose_name='javascript')),
                ('html', models.TextField(blank=True, null=True, verbose_name='html')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='store.type', verbose_name='分类')),
            ],
            options={
                'verbose_name': '代码仓库',
                'verbose_name_plural': '代码仓库',
            },
        ),
    ]