import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Camp(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField(max_length=400, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    user_created = models.ForeignKey(User, related_name='camps_created')
    owners = models.ManyToManyField(User, related_name='camps_owned')

    class Meta:
        verbose_name = 'Camp'
        verbose_name_plural = 'Camps'

    def get_absolute_url(self):
        return reverse('camp_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


def get_year_choices():
    # This code from http://stackoverflow.com/questions/1517474
    YEAR_CHOICES = []
    for r in range(datetime.datetime.now().year, (datetime.datetime.now().year+3)):
        YEAR_CHOICES.append((r,r))
    return YEAR_CHOICES


class CampYear(models.Model):

    year = models.IntegerField('year', choices=get_year_choices(), default=datetime.datetime.now().year)
    camp = models.ForeignKey(Camp, related_name="years")

    class Meta:
        verbose_name = 'CampYear'
        verbose_name_plural = 'CampYears'

    def __str__(self):
        return '{} {}'.format(self.camp, self.year)
