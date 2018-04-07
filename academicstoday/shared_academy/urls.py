# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from shared_academy import views


urlpatterns = (
    url(r'^academy/create/done$', views.create_done_page, name='at_shared_academy_create_done'),
    url(r'^academy/create$', views.create_page, name='at_shared_academy_create'),
)
