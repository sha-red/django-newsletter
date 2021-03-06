# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-29 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_auto_20180524_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='language',
            field=models.CharField(choices=[('de', 'German'), ('en', 'English')], default='de', max_length=5, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='publish_date',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, null=True, verbose_name='release date'),
        ),
    ]
