# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login/")
def create_page(request):
    return render(request, 'shared_academy/create_view.html',{
        'current_page': 'home-master',
    })


@login_required(login_url="login/")
def create_done_page(request):
    return render(request, 'shared_academy/create_finished_view.html',{
        'current_page': 'home-master',
    })
