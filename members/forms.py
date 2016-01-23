from django import forms
from members.models import MemberInvitation


class MemberInvitationForm(forms.ModelForm):
    class Meta:
        model = MemberInvitation
        fields = ['recipient_email', 'permissions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient_email'].label = ''
        self.fields['recipient_email'].help_text = None
        self.fields['permissions'].label = ''
        self.fields['permissions'].help_text = None
