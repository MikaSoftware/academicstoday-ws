# -*- coding: utf-8 -*-
import csv
from datetime import date, datetime, timedelta
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_tenants.models import TenantMixin, DomainMixin
from shared_foundation import constants
from shared_foundation.models.abstract_thing import AbstractSharedThing
from shared_foundation.models.abstract_contact_point import AbstractSharedContactPoint
from shared_foundation.models.abstract_postal_address import AbstractSharedPostalAddress
from shared_foundation.models.abstract_geo_coorindate import AbstractSharedGeoCoordinate
from shared_foundation.models.user import SharedUser


class SharedAcademyManager(models.Manager):
    def delete_all(self):
        items = SharedAcademy.objects.all()
        for item in items.all():
            item.delete()


class SharedAcademy(TenantMixin, AbstractSharedThing, AbstractSharedContactPoint, AbstractSharedPostalAddress, AbstractSharedGeoCoordinate):
    """
    Model is the tenant in our system.
    """

    class Meta:
        app_label = 'shared_foundation'
        db_table = 'at_academies'
        verbose_name = _('Franchise')
        verbose_name_plural = _('Franchises')
        default_permissions = ()
        permissions = (
            ("can_get_academys", "Can get academys"),
            ("can_get_academy", "Can get academy"),
            ("can_post_academy", "Can post academy"),
            ("can_put_academy", "Can put academy"),
            ("can_delete_academy", "Can delete academy"),
        )

    objects = SharedAcademyManager()

    #
    #  Custom Fields
    #

    activation_callback_url = models.URLField(
        _("Activation Callback URL"),
        help_text=_('The URL which will be presented to the user in the activation email.'),
        null=True,
        blank=True
    )

    reset_password_callback_url = models.URLField(
        _("Reset Password Callback URL"),
        help_text=_('The URL which will be presented to the user was requested a password reset url in the email.'),
        null=True,
        blank=True
    )


    #
    #  FUNCTIONS
    #

    def __str__(self):
        return str(self.name)

    def reverse(self, reverse_id, reverse_args=[]):
        return settings.AT_APP_HTTP_PROTOCOL + str(self.schema_name) + "." + settings.AT_APP_HTTP_DOMAIN + reverse(reverse_id, args=reverse_args)

    def is_public(self):
        """
        Function returns boolean value as to whether this academy is the
        public or a tenant.
        """
        return self.schema_name == "public" or self.schema_name == "test"

class SharedAcademyDomain(DomainMixin):
    class Meta:
        app_label = 'shared_foundation'
        db_table = 'atacademy_domains'
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')

    pass
