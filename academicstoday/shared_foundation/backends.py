# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class AcademicsTodayTenantedEmailBackend(ModelBackend):
    def authenticate(self, username="", password="", **kwargs):
        """Allow users to log in with their email address."""
        try:
            # Assign the "username" which is our "email" to the identifier object
            # which we will use to lookup.
            identifier = None
            if kwargs['academy']:
                identifier = kwargs['academy'] + "|" + username
            else:
                identifier = "0|" + username

            # Lookup our user based on the unique `identifier` field.
            user = get_user_model().objects.filter(identifier__iexact=identifier)[0]

            if check_password(password, user.password):
                return user
            else:
                return None

        except IndexError:
            # No user was found, return None - triggers default login failed
            return None
