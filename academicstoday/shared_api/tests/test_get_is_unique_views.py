# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.db.models import Q
from django.db import transaction
from django.test import TestCase
from django.test import Client
from django.utils import translation
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from shared_foundation import constants
from shared_foundation.models import SharedUser


TEST_USER_EMAIL = "bart@academicstoday.com"
TEST_USER_USERNAME = "bart@academicstoday.com"
TEST_USER_PASSWORD = "123P@$$w0rd"
TEST_USER_TEL_NUM = "123 123-1234"
TEST_USER_TEL_EX_NUM = ""
TEST_USER_CELL_NUM = "123 123-1234"


class GetIsUniqueWithPublicSchemaTestCase(APITestCase, TenantTestCase):
    """
    Console:
    python manage.py test shared_api.tests.test_get_is_unique_views
    """
    @transaction.atomic
    def setUp(self):
        translation.activate('en')  # Set English
        super(GetIsUniqueWithPublicSchemaTestCase, self).setUp()
        self.c = TenantClient(self.tenant)
        call_command('init_app', verbosity=0)
        call_command(
           'create_shared_account',
           TEST_USER_EMAIL,
           TEST_USER_PASSWORD,
           "Bart",
           "Mika",
           verbosity=0
        )

    @transaction.atomic
    def tearDown(self):
        users = SharedUser.objects.all()
        for user in users.all():
            user.delete()
        del self.c
        super(GetIsUniqueWithPublicSchemaTestCase, self).tearDown()

    @transaction.atomic
    def test_anonymous_get_with_200(self):
        # CASE 1 OF 2:
        url = reverse('at_get_is_unique_api_endpoint')+"?email="+TEST_USER_EMAIL
        response = self.c.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, int(response.content))

        # CASE 2 OF 2:
        url = reverse('at_get_is_unique_api_endpoint')+"?email=trudy@academicstoday.com"
        response = self.c.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, int(response.content))
