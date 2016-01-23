
from django.conf.urls import include, patterns, url
from members.views import MemberListView, MemberInviteView

urlpatterns = patterns('members.views',

    url(r'^$', MemberListView.as_view(), name="member_list"), # List all members for the year
    url(r'^invite$', MemberInviteView.as_view(), name="member_invite"), # Invite new members for the year
)

