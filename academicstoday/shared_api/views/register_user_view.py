import django_filters
import django_rq
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from django_filters import rest_framework as filters
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import mixins # See: http://www.django-rest-framework.org/api-guide/generic-views/#mixins
from rest_framework import authentication, viewsets, permissions, status, parsers, renderers
from rest_framework.decorators import detail_route, list_route # See: http://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
from rest_framework.response import Response
from shared_foundation import models
from shared_foundation import utils
from shared_api.serializers.register_user_serializers import RegisterUserSerializer
from shared_auth.tasks import send_user_activation_email_func


class RegisterUserAPIView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        # Perform validation.
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Attempt to create a user and return status.
        try:
            user = models.SharedUser.objects.create(
                identifier="0|"+serializer.validated_data['email'], # CUSTOM FORMAT.
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],
                is_active=False,
                was_email_activated=False
            )

            # Generate and assign the password.
            user.set_password(serializer.validated_data['password'])
            user.save()

            # Send an email.
            django_rq.enqueue(send_user_activation_email_func, user.email)

            print("---------------------")
            print("PUBLIC: Created user.")
            print("---------------------")

            # Implemented response.
            return Response({
                'status': 'Registered',
                'reason': ''
            })
        except Exception as e:
            return Response({
                'status': 'Failed',
                'reason': str(e)
            })
