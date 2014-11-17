# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import logging

from haystack.management.commands import update_index

from celery import task

logger = logging.getLogger(__name__)


@task()
def update_search_index():
    logger.info('update_search_index')
    update_index.Command().handle()
