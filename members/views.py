from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from members.models import Membership, MemberInvitation
from members.forms import MemberInvitationForm
from camps.models import CampYear
from base.mixins import CamperBaseMixin
from extra_views import InlineFormSetView
from datetime import timedelta
from django.conf import settings

class MemberListView(CamperBaseMixin, ListView):
    """Lists members visible to the user"""
    model = Membership


class MemberInviteView(CamperBaseMixin, InlineFormSetView):
    model = CampYear
    inline_model = MemberInvitation
    form_class = MemberInvitationForm
    fields = ['recipient_email', 'permissions']
    can_delete = False
    extra = 10
    template_name = 'members/invitation_form.html'

    def formset_valid(self, formset):
        campyear = get_object_or_404(CampYear, camp_id=self.kwargs.get('pk'), year=self.kwargs.get('year'))
        invitations = formset.save(commit=False)
        for invitation in invitations:
            invitation.campyear = campyear
            invitation.sender = self.request.user
            invitation.time_limit = timedelta(days=settings.INVITATION_DEFAULT_DURATION_DAYS)
            invitation.save()
        return super().formset_valid(formset)

