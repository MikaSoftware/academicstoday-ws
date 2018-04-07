from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import serializers, viewsets, routers
from shared_api.views.auth_login_view import LoginAPIView
from shared_api.views.auth_logout_view import LogoutAPIView
from shared_api.views.auth_send_reset_password_email_views import SendResetPasswordEmailAPIView
from shared_api.views.auth_reset_password_views import ResetPasswordAPIView
from shared_api.views.academy_list_views import SharedAcademyListAPIView
from shared_api.views.get_is_unique_views import GetIsUniqueAPIView
from shared_api.views.register_user_view import RegisterUserAPIView
# from shared_api.views.register_university_view import RegisterUniversityAPIView


urlpatterns = [
    #----------------------#
    # Shared API-endpoints #
    #----------------------#

    url(r'^api/register/user/$', RegisterUserAPIView.as_view()),

    # University
    # url(r'^api/register/university/$', RegisterUniversityAPIView.as_view()),

    # Authentication.
    url(r'^api/login$', LoginAPIView.as_view(), name='at_login_api_endpoint'),
    url(r'^api/logout$', LogoutAPIView.as_view(), name='at_logout_api_endpoint'),
    url(r'^api/reset-password$', ResetPasswordAPIView.as_view(), name='at_reset_password_api_endpoint'),
    url(r'^api/send-reset-password-email$', SendResetPasswordEmailAPIView.as_view(), name='at_send_reset_password_email_api_endpoint'),

    # Functions.
    url(r'^api/get_is_unique$', GetIsUniqueAPIView.as_view(), name='at_get_is_unique_api_endpoint'),

    # Application.
    url(r'^api/academys$', SharedAcademyListAPIView.as_view(), name='at_academy_list_api_endpoint'),

    # JWT
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]


urlpatterns = format_suffix_patterns(urlpatterns)
