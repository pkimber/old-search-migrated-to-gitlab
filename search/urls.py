# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns
from django.conf.urls import url

from haystack.forms import SearchForm
from haystack.views import search_view_factory

from .views import MySearchView


urlpatterns = patterns(
    '',
    url(regex=r'^search/$',
        view=search_view_factory(
            form_class=SearchForm,
            view_class=MySearchView,
        ),
        name='search.search'
        ),
)
