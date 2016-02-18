from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CampYearForm, CampForm
from .models import Camp, CampYear

from base.mixins import CamperBaseMixin, AuthorshipFormViewMixin


class CampBaseMixin(CamperBaseMixin):
    model = Camp


class CampEditBaseMixin(CampBaseMixin, SuccessMessageMixin, AuthorshipFormViewMixin):
    form_class = CampForm
    template_name = 'camps/camp_form.html'
    success_message = "Your camp %(name)s was %(verb)sed successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            verb=self.success_verb,
        )


class CampCreateView(CampEditBaseMixin, CreateView):
    success_verb = 'create'

    def form_valid(self, form):
        super().form_valid(form)
        camp_year = CampYear(year=form.cleaned_data['first_year'])
        camp_year.camp = self.object
        camp_year.save()
        return HttpResponseRedirect(self.get_success_url())


class CampUpdateView(CampEditBaseMixin, UpdateView):
    success_verb = 'edit'

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class CampDetailView(CampBaseMixin, DetailView):
    template_name = 'camps/camp_detail.html'
    model = Camp


class CampListView(CampBaseMixin, ListView):
    template_name = 'camps/camp_list.html'
    model = Camp

