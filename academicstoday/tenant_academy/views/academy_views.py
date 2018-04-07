# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login/")
def retrieve_page(request):
    return render(request, 'tenant_academy/academy_views/retrieve_view.html',{
        'current_page': 'home-master',
        'tenant': request.tenant
    })
