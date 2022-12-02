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
from ..forms import AdminSignUpForm, AppointmentForm
from ..models import User, Admin, Customer, Pet, Appointment, Publication, PetWatcher

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
        context['petwatchers'] = PetWatcher.objects.all()
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

@login_required
@admin_required
def change_status(request, pk, type):
    # get the appointment and change the status
    appointment = Appointment.objects.get(id=pk)
    if type == 'Cancelado':
        appointment.status = 'Cancelado'
    elif type == 'Aceptado':
        appointment.status = 'Aceptado'
    elif type == 'Completado':
        appointment.status = 'Completado'
    appointment.save()
    messages.success(request, 'El estado del servicio ha sido cambiado')
    return redirect('admins:service_admins')

@login_required
@admin_required
def delete_appointment(request, pk):
    # get the appointment and delete
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    messages.success(request, 'El servicio ha sido eliminado')
    return redirect('admins:service_admins')

@login_required
@admin_required
def update_appointment(request, pk):
    # get the appointment and update
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('admins:service_admins')
    context = {'form': form}
    return render(request, 'pet_hotel/admins/appointment_form.html', context)


@method_decorator([login_required, admin_required], name='dispatch')
class PetWatcherCheckView(DetailView):
    model = PetWatcher
    template_name = 'pet_hotel/admins/petwatcher_check.html'
    

@login_required
@admin_required
def delete_petwatcher(request, pk):
    # get the petwatcher and delete
    petwatcher = PetWatcher.objects.get(id=pk)
    # and get the customer of the petwatcher and change is_the_dog_watcher to False
    customer = Customer.objects.get(user_id=petwatcher.customer.user_id)
    customer.is_dog_watcher = False
    customer.save()
    petwatcher.delete()
    messages.success(request, 'El paseador ha sido eliminado')
    return redirect('admins:profile_admins')

@login_required
@admin_required
def customer_is_dog_watcher(request, pk):
    # get the customer of the petwatcher and change is_the_dog_watcher to True
    petwatcher = PetWatcher.objects.get(id=pk)
    customer = Customer.objects.get(user_id=petwatcher.customer.user_id)
    customer.is_dog_watcher = True
    customer.save()
    petwatcher.accepted = True
    petwatcher.save()
    messages.success(request, 'El cliente ha sido cambiado a paseador')
    return redirect('admins:profile_admins')


