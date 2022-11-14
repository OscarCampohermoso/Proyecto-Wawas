from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from pet_hotel.models import User, Customer


class CustomerSignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=200, required=True)
    dirección = forms.CharField(max_length=200, required=True)
    telefono = forms.CharField(max_length=200, required=True)
    email = forms.CharField(max_length=200, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.name = self.cleaned_data.get('nombre')
        customer.address = self.cleaned_data.get('dirección')
        customer.phone = self.cleaned_data.get('telefono')
        customer.email = self.cleaned_data.get('email')
        customer.save()
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user
