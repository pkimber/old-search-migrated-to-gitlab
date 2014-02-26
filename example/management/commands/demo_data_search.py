# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core import management
from django.core.management.base import BaseCommand

from example.models import Cake, Coffee


class Command(BaseCommand):

    help = "Create demo data for 'search'"

    def handle(self, *args, **options):
        # setup the 'search' demo data
        self._demo_data_search()
        print("Created 'search' demo data...")

    def _demo_data_search(self):
        Cake(
            name='Lemon Cake', description='Probably... one of the best'
        ).save()
        Cake(
            name='Carrot Cake', description='My personal favourite'
        ).save()
        Cake(
            name='Coffee Cake', description='Wonderful with walnuts'
        ).save()
        Coffee(
            name='Capuccino coffee', rating=10
        ).save()
