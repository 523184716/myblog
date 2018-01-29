# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj02', '0002_auto_20180115_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='assets_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(max_length=50, verbose_name='\u670d\u52a1\u540d')),
                ('server_IP', models.GenericIPAddressField(verbose_name='\u670d\u52a1\u5668\u5730\u5740')),
                ('cpu', models.CharField(max_length=10, verbose_name='cpu')),
                ('mem', models.CharField(max_length=20, verbose_name='\u5185\u5b58')),
                ('system', models.CharField(max_length=20, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('region', models.CharField(max_length=30, verbose_name='\u673a\u623f\u533a\u57df')),
                ('create_date', models.DateTimeField(verbose_name='\u4e0a\u67b6\u65e5\u671f')),
                ('remarks', models.TextField(max_length=200, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('IP', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='serveradmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='uaseradmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=1, choices=[(1, 'man'), (2, 'women'), (3, 'zhong')])),
            ],
        ),
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=256)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='grade',
            field=models.ForeignKey(to='dj02.serveradmin'),
        ),
    ]
