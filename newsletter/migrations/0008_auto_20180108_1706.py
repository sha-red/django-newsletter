# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_newsletter_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='language',
            field=models.CharField(choices=[('de', 'German'), ('en', 'English')], default='de', max_length=5, verbose_name='language'),
        ),
    ]