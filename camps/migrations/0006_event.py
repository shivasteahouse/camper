# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

event_fixture =  [
  {
    "pk": 1,
    "name": "Burning Man"
  },
  {
    "pk": 2,
    "name": "Blazing Swan"
  }
]

def load_events(apps, schema_editor):
    Event = apps.get_model("camps", "Event")
    for event in event_fixture:
        Event.objects.create(**event)

def delete_events(apps, schema_editor):
    Event = apps.get_model("camps", "Event")
    Event.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0005_auto_20160123_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RunPython(load_events, delete_events),
    ]
