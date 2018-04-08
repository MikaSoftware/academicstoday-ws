# -*- coding: utf-8 -*-
import phonenumbers
from datetime import datetime, timedelta
from dateutil import tz
from starterkit.drf.validation import (
    MatchingDuelFieldsValidator,
    EnhancedPasswordStrengthFieldValidator
)
from starterkit.utils import (
    get_random_string,
    get_unique_username_from_email
)
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.db.models import Q, Prefetch
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote
from rest_framework import exceptions, serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from shared_api.custom_fields import PhoneNumberField
from shared_foundation.models import SharedUser
# from tenant_api.serializers.customer_comment import CourseCommentSerializer
from tenant_foundation.models import (
    # Comment,
    # CourseComment,
    Course
)


class CourseListCreateSerializer(serializers.ModelSerializer):

    # Meta Information.
    class Meta:
        model = Course
        fields = (
            # Thing
            'id',
            'created_at',
            'last_modified_at',
        )

    # def setup_eager_loading(cls, queryset):
    #     """ Perform necessary eager loading of data. """
    #     queryset = queryset.prefetch_related(
    #         'owner', 'created_by', 'last_modified_by',
    #         # 'comments'
    #     )
    #     return queryset

    def create(self, validated_data):
        """
        Override the `create` function to add extra functinality:

        -TODO
        """


        # Return our validated data.
        return validated_data


class CourseRetrieveUpdateDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            # Thing
            'id',
            'created_at',
            'last_modified_at'
        )

    # def setup_eager_loading(cls, queryset):
    #     """ Perform necessary eager loading of data. """
    #     queryset = queryset.prefetch_related(
    #         'owner', 'created_by', 'last_modified_by',
    #         # 'comments'
    #     )
    #     return queryset

    def update(self, instance, validated_data):
        """
        Override this function to include extra functionality.
        """
        # For debugging purposes only.
        # print(validated_data)

        # Return our validated data.
        return validated_data
