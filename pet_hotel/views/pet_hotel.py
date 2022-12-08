from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from pet_hotel.forms import ContactForm
from pet_hotel.models import Contact, Publication
from django.core.mail import send_mail
from django.conf import settings
from django.utils.decorators import method_decorator
from ..forms import CustomerSignUpForm, AppointmentForm, PublicationForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from ..models import User, Customer, Pet, Appointment, Publication
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admins:profile_admins')
        else:
            return redirect('customers:profile_customers')
    else:
        return render(request, 'pet_hotel/home.html')

def service(request):
    return render(request, 'pet_hotel/service.html')

'''Para ver la tabla de mensajes de Contactos'''
'''def contact_admin(request):
    contacts = Contact.objects.all()
    return render(request, 'pet_hotel/contact_admin.html',{"messages_contacts":contacts})
'''
def contact(request):
    data = {
        'contact_form':ContactForm()
    }
    # if user is logged in put the user email in the email field
    if request.user.is_authenticated:
        data['contact_form'].fields['email'].initial = request.user.email

    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        message += ' - Mensaje enviado por:  ' + email
        send_mail(
            name, #asunto 
            message, #message
            'settings.EMAIL_HOST_USER',
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        messages.success(request, 'Mensaje enviado correctamente')
    return render(request, 'pet_hotel/contact.html', data)
############################################################################################################
def news(request):
    publications = Publication.objects.all()
    # Order by publication.date_of_creation 
    publications = publications.order_by('-date_of_creation')
    return render(request, 'pet_hotel/news.html', {'publications': publications})

@method_decorator(login_required, name='dispatch')
class CreatePublicationView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'pet_hotel/customers/publication_form.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        publication = form.save(commit=False)
        publication.user = self.request.user
        publication.save()
        messages.success(self.request, 'Publicación creada correctamente')
        return super().form_valid(form)


@login_required
def update_publication(request, id):
    publication = Publication.objects.get(id=id)
    data = {
        'form': PublicationForm(instance=publication)
    }

    if request.method == 'POST':
        form = PublicationForm(data=request.POST, instance=publication, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación actualizada correctamente')
            return redirect('news')
        data['form'] = form
    return render(request, 'pet_hotel/customers/publication_form.html', data)


@login_required
def delete_publication(request, id):
    publication = Publication.objects.get(id=id)
    publication.delete()
    messages.success(request, 'Publicación eliminada correctamente')
    return redirect('news')





