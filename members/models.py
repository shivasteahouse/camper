from django.db import models
from django.contrib.auth.models import User
from camps.models import Camp


class Member(models.Model):
	user = models.OneToOneField(User, related_name='member')
	join_date = forms.DateTimeField(auto_now_add=True)
	camp = models.ForeignKey(Camp, related_name='members')

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __unicode__(self):
        return self.user.first_name
