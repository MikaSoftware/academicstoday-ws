# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from tenant_academy.views import academy_views, student_views


urlpatterns = (
    # Academy views
    url(r'^info/$', academy_views.retrieve_page, name='at_tenant_academy_retrieve'),

    # Student views
    url(r'^student/register/finished$', student_views.register_student_finished_page, name='at_tenant_academy_student_register_finished'),
    url(r'^student/register$', student_views.register_student_page, name='at_tenant_academy_student_register'),
    url(r'^students/$', student_views.StudentListView.as_view(), name='at_tenant_academy_student_list'),
    url(r'^student/<int:pk>/$', student_views.StudentRetrieveView.as_view(), name='at_tenant_academy_student_retrieve'),
)
