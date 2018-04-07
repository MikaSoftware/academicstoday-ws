# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login/")
def dashboard_page(request):
    """
    The default entry point into our application.
    """
    return render(request, 'shared_dashboard/view.html',{
        'current_page': 'home-master',
    })
