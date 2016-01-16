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


class MemberInvitation(models.Model):
    """
    An invitation sent to an email address to invite someone to join a camp.

    """

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('expired', 'Expired'),
    )

    INVITE_PERMS_CHOICES = (
        ('normal', 'Normal'),
        ('admin_user', 'Camp Manager'),
    )

    campyear = models.ForeignKey(CampYear, related_name='invitations')
    sender = models.ForeignKey(User, related_name='invitations')
    recipient_email = models.EmailField(unique=True, help_text="The email address of the person you are inviting to join your camp.")
    permissions =  models.CharField('Permissions', choices=INVITE_PERMS_CHOICES, max_length=10, default="normal",
        help_text='The level of access you want to grant to this user.' )
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Invitation Status', choices=STATUS_CHOICES, max_length=8, default="pending")
    status_change_time = models.TimeField(auto_now=True)
    time_limit = models.DurationField()

    class Meta:
        verbose_name = 'MemberInvitation'
        verbose_name_plural = 'MemberInvitations'

    def get_sender(self): # A workaround for the post_save receiver which also uses 'sender' as a keyword
        return self.sender

    def __unicode__(self):
        return "Invitation to {} to join camp {} from {}".format(self.recipient_email, self.campyear, self.sender)

