# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('the_pantry', '0003_auto_20180308_1401'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post',
            new_name='recipe',
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name_plural': 'Recipies'},
        ),
    ]