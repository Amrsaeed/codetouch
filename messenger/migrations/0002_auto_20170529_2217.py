# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sent',
            new_name='sentOn',
        ),
        migrations.AddField(
            model_name='message',
            name='reciever',
            field=models.CharField(default='None', max_length=150),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default='None', max_length=150),
        ),
    ]