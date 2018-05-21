# -*- coding: utf-8 -*-
"""
Delete all unsubscribed subscribers from the database.
"""
import logging

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _


class Command(BaseCommand):
    help = _("Delete all unsubscribed subscribers from the database..")

    def handle(self, *args, **options):
        # Setup logging based on verbosity: 1 -> INFO, >1 -> DEBUG
        verbosity = int(options['verbosity'])
        logger = logging.getLogger('newsletter')
        if verbosity == 0:
            logger.setLevel(logging.WARN)
        elif verbosity == 1:  # default
            logger.setLevel(logging.INFO)
        elif verbosity > 1:
            logger.setLevel(logging.DEBUG)
        if verbosity > 2:
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)

        logger.info(_('Deleting all unsubscribed subscribers from the database'))

        raise NotImplementedError
