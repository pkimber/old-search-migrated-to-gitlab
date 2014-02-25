# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Cake'
        verbose_name_plural = 'Cakes'

    def __str__(self):
        return unicode('{}'.format(self.name))

    def get_summary_description(self):
        return filter(None, (
            self.name,
            self.description,
        ))


class Coffee(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Coffee'
        verbose_name_plural = 'Coffees'

    def __str__(self):
        return unicode('{}'.format(self.name))

    def get_summary_description(self):
        return filter(None, (
            self.name,
            self.rating,
        ))
