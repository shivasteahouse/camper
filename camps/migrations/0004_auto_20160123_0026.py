# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0003_camp_owners'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campyear',
            options={'get_latest_by': 'year', 'verbose_name': 'CampYear', 'verbose_name_plural': 'CampYears'},
        ),
        migrations.AlterField(
            model_name='campyear',
            name='year',
            field=models.IntegerField(verbose_name='year', choices=[(2016, 2016), (2017, 2017), (2018, 2018)], default=2016),
        ),
    ]
