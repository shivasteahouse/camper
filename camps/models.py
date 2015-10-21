from django.db import models
from django.contrib.auth.models import User
import datetime


class Camp(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField(max_length=400, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    user_created = models.ForeignKey(User, related_name='camps_created')
    owners = models.ManyToManyField(User, related_name='camps_owned')

    class Meta:
        verbose_name = 'Camp'
        verbose_name_plural = 'Camps'

    def __unicode__(self):
        return self.name


class CampYear(models.Model):
    YEAR_CHOICES = []
    for r in range(2016, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    year = models.IntegerField('year', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    camp = models.ForeignKey(Camp, related_name="years")

    class Meta:
        verbose_name = 'CampYear'
        verbose_name_plural = 'CampYears'

    def __unicode__(self):
        return '{} {}'.format(self.camp, self.year)
