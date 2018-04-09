# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from shared_foundation.models import SharedUser


@login_required(login_url="login/")
def create_course_page(request):
    return render(request, 'tenant_academy/course_views/create_view.html',{
        'current_page': 'home-master',
        'tenant': request.tenant
    })
