from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from ..decorators import customer_required
from ..forms import CustomerSignUpForm
from ..models import User, Customer, Pet

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('customers:profile_customers')


@method_decorator([login_required, customer_required], name='dispatch')
class ProfileCustomerView(UpdateView):
    model = Customer
    template_name = 'pet_hotel/customers/profile_customer.html'
    fields = ['name', 'address', 'phone', 'email', 'profile_image']
    success_url = reverse_lazy('customers:profile_customers')

    def get_form(self, form_class=None):
        form = super(ProfileCustomerView, self).get_form()
        form.fields['name'].label = 'Nombre'
        form.fields['address'].label = 'Dirección'
        form.fields['phone'].label = 'Teléfono'
        form.fields['email'].label = 'Correo'
        form.fields['profile_image'].label = 'Imagen de perfil'
        return form

    
    # get pets model
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.filter(customer=self.request.user.customer)
        return context

    def get_object(self):
        return self.request.user.customer

def delete_pets(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    messages.success(request, 'Mascota eliminada')
    return redirect('customers:profile_customers')

@login_required
@customer_required
def news(request):
    return render(request, 'pet_hotel/customers/news_customer.html')

@login_required
@customer_required
def service(request):
    return render(request, 'pet_hotel/customers/service_customer.html')


# @method_decorator([login_required, customer_required], name='dispatch')
# class ApointmentCustomerView(CreateView):