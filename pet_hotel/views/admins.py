from django.contrib import messages, admin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
                        
from ..decorators import admin_required
from ..forms import AdminSignUpForm
from ..models import User, Admin, Customer, Pet, Appointment, Publication

class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admins:profile_admins')

# all users in list view
@method_decorator([login_required, admin_required], name='dispatch')
class UserListView(ListView):
    model = User
    # only if the user has is_customer = True
    queryset = User.objects.filter(is_customer=True, is_active=True)

    context_object_name = 'users'
    template_name = 'pet_hotel/admins/profile_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context

@login_required
@admin_required
def edit_status(request, pk):
    # get the user and change the status
    user = User.objects.get(id=pk)
    user.is_active = not user.is_active
    user.save()
    messages.success(request, 'El estado del usuario ha sido cambiado')
    return redirect('admins:profile_admins')

@method_decorator([login_required, admin_required], name='dispatch')
class ServiceListView(ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'pet_hotel/admins/service_admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.all()
        return context

@method_decorator([login_required, admin_required], name='dispatch')
class AppointmentCheckView(DetailView):
    model = Appointment
    template_name = 'pet_hotel/admins/appointment_check.html'
