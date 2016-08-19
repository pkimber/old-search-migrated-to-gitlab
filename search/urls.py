# -*- encoding: utf-8 -*-
from django.conf.urls import url

from haystack.views import search_view_factory

from .forms import MySearchForm
from .views import MySearchView


urlpatterns = [
    url(regex=r'^search/$',
        view=search_view_factory(
            form_class=MySearchForm,
            view_class=MySearchView,
        ),
        name='search.search'
        ),
]
