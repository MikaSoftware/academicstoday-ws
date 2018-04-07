# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shared_foundation.decorators import public_only_or_redirect
from shared_foundation.models import SharedAcademy


@public_only_or_redirect
@login_required(login_url="login/")
def dashboard_page(request):
    academies = SharedAcademy.objects.filter(owner=request.user)
    return render(request, 'shared_dashboard/view.html',{
        'current_page': 'home-master',
        'academies': academies
    })
