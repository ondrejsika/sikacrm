# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-27 22:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='name',
            field=models.CharField(default='<default>', max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='workspace',
            unique_together=set([('name', 'user')]),
        ),
    ]
