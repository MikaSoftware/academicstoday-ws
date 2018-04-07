# -*- coding: utf-8 -*-
import os
import sys
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _
from django.core.management import call_command
from shared_foundation.constants import *


class Command(BaseCommand):
    """
    Console:
    python manage.py init_app
    """
    help = _('Command will setup the application database to be ready for usage.')

    def handle(self, *args, **options):
        self.process_site()
        self.process_groups()
        self.stdout.write(
            self.style.SUCCESS(_('Successfully initialized application.'))
        )

    def process_site(self):
        """
        Site
        """
        current_site = Site.objects.get_current()
        current_site.domain = settings.AT_APP_HTTP_DOMAIN
        current_site.name = "AcademicsToday.io"
        current_site.save()

    def process_groups(self):
        pass #TODO: IMPL.
