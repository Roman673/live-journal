# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0010_auto_20170831_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='learning_logs/img'),
        ),
    ]
