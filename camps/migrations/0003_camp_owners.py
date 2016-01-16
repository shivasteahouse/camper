# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camps', '0002_auto_20151021_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='camps_owned'),
        ),
    ]
