from django.shortcuts import render
from django.views.edit import CreateView, UpdateView
from django.views.generics import ListView
from models import Membersip
# Create your views here.


class MemberListView(ListView):
    """Lists members visible to the user"""
    model = Membership



