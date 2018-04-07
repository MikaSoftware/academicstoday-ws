# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from shared_dashboard import views


urlpatterns = (
    url(r'^dashboard$', views.dashboard_page, name='at_dashboard_master'),
)
