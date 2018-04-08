from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, serializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from shared_foundation import models
from shared_foundation import utils


class ActivateSerializer(serializers.Serializer):
    pr_access_code = serializers.CharField(
        allow_blank=False,
        max_length=255,
        trim_whitespace=True
    )

    def validate(self, attrs):
        pr_access_code = attrs.get('pr_access_code', None)
        if pr_access_code is None:
            raise serializers.ValidationError("Pr code not entered.")

        user = models.SharedUser.objects.filter(pr_access_code=pr_access_code).first()
        if user is None:
            raise serializers.ValidationError("Pr code does not exist.")

        if user.has_pr_code_expired():
            raise serializers.ValidationError("Pr code code has expired.")

        attrs['user'] = user
        
        return attrs
