# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login/")
def register_student_page(request):
    return render(request, 'tenant_academy/student_views/register_student_view.html',{
        'current_page': 'home-master',
        'tenant': request.tenant
    })


@login_required(login_url="login/")
def register_student_finished_page(request):
    return render(request, 'tenant_academy/student_views/register_student_view.html',{
        'current_page': 'home-master',
        'tenant': request.tenant
    })
