# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('first_review_date', models.DateTimeField(verbose_name='date first reviewed')),
                ('last_review_date', models.DateTimeField(verbose_name='date last reviewed')),
                ('permanently_closed', models.IntegerField(default=0)),
            ],
        ),
    ]
