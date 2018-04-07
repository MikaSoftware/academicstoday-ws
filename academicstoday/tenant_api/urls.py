from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import serializers, viewsets, routers
from tenant_api.views.registrar_view import RegistrarAPIView


urlpatterns = [
    url(r'^api/registrar/$', RegistrarAPIView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
