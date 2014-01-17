from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

from haystack.views import SearchView


class MySearchView(SearchView):

    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context.update(dict(
        ))
        return context

    def create_response(self):
        """
        Check that a user is logged in and a member of staff.

        Note: Can't use the standard 'braces' decorators as the Haystack views
        are not like the standard class based views.
        """
        if self.request.user.is_authenticated():
            if not self.request.user.is_staff:
                raise PermissionDenied  # return a forbidden response
            return super(MySearchView, self).create_response()
        else:
            return redirect_to_login(self.request.path, settings.LOGIN_URL)
