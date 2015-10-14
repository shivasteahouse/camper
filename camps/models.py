from django.db import models
from django.contrib.auth.models import User


class Camp(models.Model):
	name = models.CharField('Name', max_length=50)
	description = models.TextField(max_length=400, blank=True)
	creation_time = models.DateTimeField(auto_now_add=True)
	user_created = models.ForeignKey(User, related_name='camps_created')

    class Meta:
        verbose_name = 'Camp'
        verbose_name_plural = 'Camps'

    def __unicode__(self):
        return self.name

