# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camps', '0004_auto_20160123_0026'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInvitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('recipient_email', models.EmailField(unique=True, help_text='The email address of the person you are inviting to join your camp.', max_length=254)),
                ('permissions', models.CharField(verbose_name='Permissions', choices=[('normal', 'Normal'), ('admin_user', 'Camp Manager')], help_text='The level of access you want to grant to this user.', max_length=10, default='normal')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(verbose_name='Invitation Status', choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('expired', 'Expired')], default='pending', max_length=8)),
                ('status_change_time', models.TimeField(auto_now=True)),
                ('time_limit', models.DurationField()),
                ('campyear', models.ForeignKey(related_name='invitations', to='camps.CampYear')),
                ('sender', models.ForeignKey(related_name='invitations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MemberInvitation',
                'verbose_name_plural': 'MemberInvitations',
            },
        ),
    ]
