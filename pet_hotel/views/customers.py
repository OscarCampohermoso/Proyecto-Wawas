from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.forms import SelectMultiple, Select
from django.core.mail import send_mail
# import datetime.date.today library
import datetime




from ..decorators import customer_required
from ..forms import CustomerSignUpForm, AppointmentForm, PublicationForm
from ..models import User, Customer, Pet, Appointment, Publication, PetWatcher

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
    

@method_decorator([login_required, customer_required], name='dispatch')
class PetCreateView(CreateView):
    model = Pet
    fields = ['name', 'date_of_birth', 'breed', 'size', 'description', 'image']
    template_name = 'pet_hotel/customers/pet_form.html'
    success_url = reverse_lazy('customers:profile_customers')

    def get_form(self, form_class=None):
        form = super(PetCreateView, self).get_form()
        form.fields['name'].label = 'Nombre'
        form.fields['date_of_birth'].widget.input_type = 'date'
        form.fields['date_of_birth'].label = 'Fecha de nacimiento'
        form.fields['breed'].label = 'Raza'
        # make a combobox with sizes of pets  medium or large
        CHOICES = (('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande'))
        form.fields['size'].widget = Select(choices=CHOICES)
        form.fields['size'].label = 'Tamaño'
        form.fields['description'].label = 'Descripción'
        form.fields['image'].label = 'Imagen'
        return form

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.customer = self.request.user.customer
        pet.save()
        messages.success(self.request, 'Mascota agregada correctamente')
        return redirect('customers:profile_customers')

    def __str__(self):
        return self.name

@method_decorator([login_required, customer_required], name='dispatch')
class PetUpdateView(UpdateView):
    model = Pet
    fields = ['name', 'date_of_birth', 'breed', 'size', 'description', 'image']
    template_name = 'pet_hotel/customers/pet_form.html'
    success_url = reverse_lazy('customers:profile_customers')

    def get_form(self, form_class=None):
        form = super(PetUpdateView, self).get_form()
        form.fields['name'].label = 'Nombre'
        form.fields['date_of_birth'].widget.input_type = 'date'
        form.fields['date_of_birth'].label = 'Fecha de nacimiento'
        form.fields['breed'].label = 'Raza'
        # make a combobox with sizes of pets  medium or large
        CHOICES = (('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande'))
        form.fields['size'].widget = Select(choices=CHOICES)
        form.fields['size'].label = 'Tamaño'
        form.fields['description'].label = 'Descripción'
        form.fields['image'].label = 'Imagen'
        return form

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.customer = self.request.user.customer
        pet.save()
        messages.success(self.request, 'Mascota actualizada con éxito')
        return redirect('customers:profile_customers')

    def __str__(self):
        return self.name

@login_required
@customer_required
def delete_pets(request, pk):
    pet = Pet.objects.get(id=pk)
    pet.delete()
    messages.success(request, 'Mascota eliminada correctamente')
    return redirect('customers:profile_customers')
    

@login_required
@customer_required
def service(request):
    # get all appointments as get context data only for customer that is logged in 
    # check all the appointments and compare with the current date and if the appointment.date_of_request == current date + a count
    # then pass count to the template 
    appointments = Appointment.objects.filter(customer=request.user.customer)
    count = 0
    for appointment in appointments:
        if appointment.date_of_request == datetime.date.today():
            count += 1
    if count > 3:
        messages.warning(request, 'Alcanzaste el límite de citas para hoy')
    return render(request, 'pet_hotel/customers/service_customer.html', {'appointments': appointments, 'count': count})


@login_required
@customer_required
def appointment(request, type):
    # get the customer that is logged in
    customer = Customer.objects.get(user=request.user)
    # get the pets of the customer that is logged in
    pets = Pet.objects.filter(customer=request.user.customer)
    # make a combobox with the pets of the customer
    CHOICES = []
    for pet in pets:
        CHOICES.append((pet.id, pet.name))
    if request.method == 'POST':
        form = AppointmentForm(request.POST, initial={'type': type, 'customer': customer})
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.customer = request.user.customer
            if pets:
                appointment.pet = Pet.objects.get(id=request.POST['pet'])
            appointment.save()
            messages.success(request, 'Cita creada correctamente')
            return redirect('customers:service_customers')
    else:
        form = AppointmentForm()
        form.fields['pet'].widget = Select(choices=CHOICES)
        form.fields['date'].widget.input_type = 'date'
        form.fields['time'].widget.input_type = 'time'
    return render(request, 'pet_hotel/customers/appointment_form.html', {'form': form})

    
@method_decorator([login_required, customer_required], name='dispatch')
class AppointmentCheckView(DetailView):
    model = Appointment
    template_name = 'pet_hotel/customers/appointment_check.html'

@login_required
@customer_required
def delete_appointment(request, pk):
    # change the status of the appointment to cancelled
    appointment = Appointment.objects.get(id=pk)
    appointment.status = 'Cancelada'
    appointment.save()
    messages.success(request, 'Cita cancelada correctamente')
    return redirect('customers:service_customers')

@method_decorator([login_required, customer_required], name='dispatch')
class PetWatcherCreateView(CreateView):
    model = PetWatcher
    fields = ['accept','reason', 'photo']
    template_name = 'pet_hotel/customers/pet_watcher_form.html'
    success_url = reverse_lazy('customers:service_customers')

    def get_form(self, form_class=None):
        form = super(PetWatcherCreateView, self).get_form()
        form.fields['accept'].label = 'He leído y acepto los términos y condiciones de uso'
        form.fields['reason'].label = 'Motivo por el que desea ser un cuidador'
        form.fields['photo'].label = 'Foto de identificación'
        # all the fields are required
        form.fields['accept'].required = True
        form.fields['reason'].required = True
        form.fields['photo'].required = True
        return form

    
    def form_valid(self, form):
        pet_watcher = form.save(commit=False)
        pet_watcher.customer = self.request.user.customer
        pet_watcher.save()
        messages.success(self.request, 'Pet watcher creado correctamente')
        return redirect('customers:service_customers')

    def __str__(self):
        return self.accept

@login_required
@customer_required
def customer_is_dog_watcher(request):
    # get all customers that is_dog_watcher = True
    customers = Customer.objects.filter(is_dog_watcher=True)
    return render(request, 'pet_hotel/customers/pet_watcher_list.html', {'customers': customers})


@login_required
@customer_required
def send_message(request, pk):
    # get the customer that is logged in
    customer = Customer.objects.get(user=request.user)
    # get the customer that is going to receive the message
    customer_to = Customer.objects.get(user_id=pk)
    # get the booth gmail account and send email to the customer that is going to receive the message
    email_customer = customer.email
    email_customer_to = customer_to.email
    message = "Hola te hablamos de Wawas para avisarte que un cliente necesita de tus servicios, por favor contactalo a la brevedad posible. Gracias"
    message += " el email del cliente es: " + email_customer
    asunto = "Wawas - Pet Hotel - Un cliente te necesita de tus servicios"
    send_mail(
            asunto, #asunto 
            message, #message
            'settings.EMAIL_HOST_USER',
            [email_customer_to],
            fail_silently=False,
        )
    messages.success(request, 'Mensaje enviado correctamente')
    return redirect('customers:petwatcher_list')

    




