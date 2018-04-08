# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import DetailView, ListView, TemplateView
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from shared_foundation.models import SharedUser


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


@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    context_object_name = 'student_list'
    queryset = SharedUser.objects.filter(
        is_active=True,
        type_of=1, #STUDENT.
    ).order_by('-created_at')
    template_name = 'tenant_academy/student_views/student_list_view.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = "students" # Required for navigation
        return context

    # def get_queryset(self):
    #     queryset = super(CustomerListView, self).get_queryset().order_by('given_name', 'last_name') # Get the base.
    #
    #     # The following code will use the 'django-filter'
    #     filter = CustomerFilter(self.request.GET, queryset=queryset)
    #     queryset = filter.qs
    #     return queryset


@method_decorator(login_required, name='dispatch')
class StudentRetrieveView(DetailView):
    context_object_name = 'customer'
    model = SharedUser
    template_name = 'tenant_academy/student_views/student_retrieve_view.html'

    def get_object(self):
        student = super().get_object()  # Call the superclass
        return student                  # Return the object

    def get_context_data(self, **kwargs):
        # Get the context of this class based view.
        modified_context = super().get_context_data(**kwargs)

        # Required for navigation
        modified_context['current_page'] = "students"

        # Return our modified context.
        return modified_context
