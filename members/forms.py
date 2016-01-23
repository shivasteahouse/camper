from django import forms
from members.models import MemberInvitation


class MemberInvitationForm(forms.ModelForm):
    class Meta:
        model = MemberInvitation
        fields = ['recipient_email', 'permissions']
