# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied

from haystack.views import SearchView

from base.view_utils import get_path


class MySearchView(SearchView):
    """Standard search view, but checking user is a member of staff.

    Looks like pagination doesn't work with the 'simple_backend'.
    https://github.com/toastdriven/django-haystack/issues/320
    """

    def extra_context(self):
        context = super(MySearchView, self).extra_context()
        context.update(dict(
            path=get_path(self.request.path),
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
