# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-19 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0002_auto_20180119_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_add', models.GenericIPAddressField(verbose_name='\u8bbf\u95ee\u5730\u5740')),
                ('cpu', models.CharField(blank=True, max_length=32, null=True, verbose_name='CPU\u6838\u6570')),
                ('mem', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u5185\u5b58\u5927\u5c0f')),
                ('hard', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u786c\u76d8\u5927\u5c0f')),
                ('region', models.CharField(max_length=32, verbose_name='\u6240\u5728\u533a\u57df')),
                ('positon', models.CharField(max_length=128, verbose_name='\u673a\u623f\u5730\u5740')),
                ('cabinet', models.CharField(max_length=64, verbose_name='\u5177\u4f53\u673a\u67dc\u4f4d\u7f6e')),
                ('shelf_time', models.DateField(verbose_name='\u4e0a\u67b6\u65f6\u95f4')),
                ('description', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=32, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('server_port', models.CharField(max_length=16, verbose_name='\u670d\u52a1\u7aef\u53e3')),
                ('access_type', models.CharField(max_length=32, verbose_name='\u8bbf\u95ee\u7c7b\u522b')),
            ],
        ),
        migrations.AddField(
            model_name='asset_list',
            name='server_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myarticle.Server'),
        ),
    ]