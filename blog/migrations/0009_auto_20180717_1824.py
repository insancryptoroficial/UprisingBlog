# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-17 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180717_1823'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comentarios',
            new_name='comentario',
        ),
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ('-data',)},
        ),
    ]
