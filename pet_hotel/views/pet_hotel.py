from django.shortcuts import render, redirect
from django.views.generic import TemplateView

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

def contact(request):
    return render(request, 'pet_hotel/contact.html')

def news(request):
    return render(request, 'pet_hotel/news.html')

