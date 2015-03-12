# -*- encoding: utf-8 -*-
from django import forms

from haystack.forms import SearchForm


class MySearchForm(SearchForm):
    """
    Search records (exclude 'deleted' records by default)...

    For form information... see 'Creating your own form':
    http://django-haystack.readthedocs.org/en/latest/views_and_forms.html#creating-your-own-form

    """

    deleted = forms.BooleanField(required=False)

    def search(self):

        # First, store the SearchQuerySet received from other processing.
        sqs = super(MySearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()
        # Check to see if a deleted was ticked.
        deleted = self.cleaned_data['deleted']
        if deleted:
            # return all records
            pass
        else:
            # exclude deleted records
            sqs = sqs.exclude(deleted=1)
        return sqs
