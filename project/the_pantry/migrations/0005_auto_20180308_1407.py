# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_pantry', '0004_auto_20180308_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_pantry.Category'),
        ),
    ]
