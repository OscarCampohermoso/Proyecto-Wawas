from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from pet_hotel.forms import ContactForm
from pet_hotel.models import Contact
from django.core.mail import send_mail
from django.conf import settings

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
    contacts = Contact.objects.all()
    data = {
        'contact_form':ContactForm()
    }
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name, #asunto 
            message, #message
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
        data["contact_message"]="Mensaje enviado"
    return render(request, 'pet_hotel/contact.html',data)

def news(request):
    return render(request, 'pet_hotel/news.html')

