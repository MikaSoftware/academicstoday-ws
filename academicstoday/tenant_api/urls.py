from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import serializers, viewsets, routers
from tenant_api.views.registrar_view import RegistrarAPIView
from tenant_api.views.activate_view import ActivateAPIView
from tenant_api.views.login_view import LoginAPIView
from tenant_api.views.course_view import (
    CourseCreateAPIView,
    CourseListAPIView,
    CourseRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    url(r'^api/registrar/$', RegistrarAPIView.as_view(), name='at_tenant_registrar_api_endpoint'),
    url(r'^api/activate/$', ActivateAPIView.as_view(), name='at_tenant_activate_api_endpoint'),
    url(r'^api/login/$', LoginAPIView.as_view(), name='at_tenant_login_api_endpoint'),

    # Courses
    url(r'^api/courses$', CourseCreateAPIView.as_view(), name='o55_course_create_api_endpoint'),
    url(r'^api/courses$', CourseListAPIView.as_view(), name='o55_course_list_api_endpoint'),
    url(r'^api/course/(?P<pk>[^/.]+)/$', CourseRetrieveUpdateDestroyAPIView.as_view(), name='o55_course_retrieve_update_destroy_api_endpoint'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
