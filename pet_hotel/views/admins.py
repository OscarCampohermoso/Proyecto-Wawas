from django.contrib import messages
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
from ..models import User

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

@method_decorator([login_required, admin_required], name='dispatch')
class ProfileAdminView(UpdateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'pet_hotel/admins/profile_admin.html'
    success_url = reverse_lazy('admins:profile_admins')

    def get_object(self):
        return self.request.user

