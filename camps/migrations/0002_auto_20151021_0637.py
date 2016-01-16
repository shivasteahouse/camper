# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campyear',
            name='year',
            field=models.IntegerField(verbose_name='year', default=2015),
        ),
    ]
