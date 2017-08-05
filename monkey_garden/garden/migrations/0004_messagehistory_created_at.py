# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0003_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagehistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
