# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myarticle', '0005_userlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='emai',
            field=models.EmailField(default='3322@qq.com', max_length=254),
            preserve_default=False,
        ),
    ]
