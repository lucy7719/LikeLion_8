# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-18 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='Livecast',
            new_name='livecast',
        ),
    ]
