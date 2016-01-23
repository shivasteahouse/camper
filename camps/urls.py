
from django.conf.urls import include, patterns, url
from .views import CampCreateView, CampUpdateView, CampDetailView, CampListView

urlpatterns = patterns('camps.views',
    # Using ids for now, convert to slugs later when slugfields exist on model

    url(r'^camps$', CampListView.as_view(), name="camp_list"), # List all camps
    url(r'^camps/add$', CampCreateView.as_view(), name="add_camp"), # Create new camp
    url(r'^(?P<pk>[0-9]+)$', CampDetailView.as_view(), name="camp_detail"), # Camp profile detail
    url(r'^(?P<pk>[0-9]+)/edit$', CampUpdateView.as_view(), name="camp_update" ), # Camp profile edit
    # url(r'^(?P<pk>[0-9]+)/members', ), # Camp members list
    # url(r'^(?P<pk>[0-9]+)/([0-9]{4})', ), # Camp year details
    # url(r'^(?P<pk>[0-9]+)/([0-9]{4})/members', ), # Camp year members list
    # url(r'^(?P<pk>[0-9]+)/([0-9]{4})/join', ), # Join camp year
)

