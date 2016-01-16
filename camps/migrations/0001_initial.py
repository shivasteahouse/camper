# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('user_created', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='camps_created')),
            ],
            options={
                'verbose_name': 'Camp',
                'verbose_name_plural': 'Camps',
            },
        ),
        migrations.CreateModel(
            name='CampYear',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('year', models.IntegerField(default=2015, verbose_name='year', max_length=4)),
                ('camp', models.ForeignKey(to='camps.Camp', related_name='years')),
            ],
            options={
                'verbose_name': 'CampYear',
                'verbose_name_plural': 'CampYears',
            },
        ),
    ]
