from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin


class CamperBaseMixin(LoginRequiredMixin, MultiplePermissionsRequiredMixin):
    pass


class AuthorshipFormViewMixin(object):

    def form_valid(self, form):
        """
        Saves the form to an object, but does not return an HTTP response.
        """
        self.object = form.save(commit=False)
        self.object.user_created = self.request.user
        self.object.save()
        return self.object
