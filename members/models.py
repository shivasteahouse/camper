from django.db import models
from django.contrib.auth.models import User
from camps.models import CampYear


class Membership(models.Model):
    user = models.OneToOneField(User, related_name='membership')
    join_date = models.DateTimeField(auto_now_add=True)
    year = models.ForeignKey(CampYear, related_name='members')

    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'

    @property
    def camp(self):
        return self.year.camp

    def __unicode__(self):
        return self.user.first_name

