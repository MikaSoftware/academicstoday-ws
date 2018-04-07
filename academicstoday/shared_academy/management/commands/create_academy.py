from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMultiAlternatives    # EMAILER
from django.urls import reverse
from django.conf import settings
from django.db import connection # Used for django tenants.
from django.template.loader import render_to_string    # HTML to TXT
from django.utils.translation import ugettext_lazy as _
from shared_foundation import constants
from shared_foundation import models
from shared_foundation import utils

# Ex:
# python manage.py create_academy 1 'london' 'London Arts School' 'London Arts School'

class Command(BaseCommand):
    help = 'Command will found a academy on Acadmeics Today.'

    def add_arguments(self, parser):
        parser.add_argument('user_pk', nargs='+', type=int)
        parser.add_argument('schema_name', nargs='+', type=str)
        parser.add_argument('name', nargs='+', type=str)
        parser.add_argument('alternate_name', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            user_pk = int(options['user_pk'][0])
            schema_name = options['schema_name'][0]
            name = options['name'][0]
            alternate_name = options['alternate_name'][0]
            user = models.SharedUser.objects.get(pk=user_pk)
            self.begin_processing(user, schema_name, name, alternate_name)
        except models.SharedUser.DoesNotExist:
            raise CommandError(_('AT: User does not exist with the ok: %s') % str(user_pk))

    def begin_processing(self, user, schema_name, name, alternate_name):
        # Connection needs first to be at the public schema, as this is where
        # the database needs to be set before creating a new tenant. If this is
        # not done then django-tenants will raise a "Can't create tenant outside
        # the public schema." error.
        connection.set_schema_to_public() # Switch to Public.

        # Create our Tenant and have Django-Tenants create the schema for this
        # academy in our database.
        academy = models.SharedAcademy.objects.create(
            owner=user,
            schema_name=schema_name,
            name=name,
            alternate_name=alternate_name
        )
        
        # Perform a custom post-save action.
        # Our tenant requires a domain so create it here.
        from django.contrib.sites.models import Site
        domain = models.SharedAcademyDomain()
        domain.domain = academy.schema_name + '.' + Site.objects.get_current().domain
        domain.tenant = academy
        domain.is_primary = False
        domain.save()

        self.stdout.write(
            self.style.SUCCESS(_('Successfully created tenant with schema name "%s".') % str(schema_name))
        )
