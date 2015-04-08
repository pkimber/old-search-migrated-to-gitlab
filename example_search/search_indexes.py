# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from haystack import indexes
from .models import Cake, Coffee


class CakeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Cake


class CoffeeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Coffee
