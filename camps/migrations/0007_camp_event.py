# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='event',
            field=models.ForeignKey(default=2, to='camps.Event', related_name='camps'),
            preserve_default=False,
        ),
    ]
