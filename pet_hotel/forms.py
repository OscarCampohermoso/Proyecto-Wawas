from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms import ModelForm


from pet_hotel.models import User, Customer, Contact, Admin, Pet, Appointment, Publication


class CustomerSignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=200, required=True)
    dirección = forms.CharField(max_length=200, required=True)
    telefono = forms.CharField(max_length=200, required=True)
    email = forms.CharField(max_length=200, required=True)

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
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'nombre', 'dirección', 'telefono', 'email', 'password1', 'password2')
        labels = { 'username': 'Nombre de usuario', 'nombre': 'Nombre', 'dirección': 'Dirección', 'telefono': 'Teléfono', 'email': 'Correo electrónico', 'password1': 'Contraseña', 'password2': 'Confirmar contraseña' }
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
            admin = Admin.objects.create(user=user)
            admin.save()
        return user

class ContactForm(forms.ModelForm):
    '''name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=320, required=True)
    phone = forms.CharField(max_length=999999999, required=True)
    message = forms.CharField(max_length=600, required=True)
'''
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
        'name': 'Asunto',
        'email': 'Correo Electrónico',
        'message': 'Mensaje'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('date', 'time', 'request', 'type', 'pet', 'customer')
        CHOICES =  (('Cuidadores', 'Cuidadores'), ('Peluqueria', 'Peluqueria'), ('Veterinaria', 'Veterinaria'))

        labels = {
        'date': 'Fecha',
        'time': 'Hora',
        'request': 'Solicitud (opcional)',
        'type': 'Tipo de servicio',
        'pet': 'Mascota (opcional)',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'time': forms.TimeInput(attrs={'class':'form-control'}),
            'request': forms.Textarea(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}, choices=CHOICES),
            'pet': forms.Select(attrs={'class':'form-control'}),
            # hide customer field
            'customer': forms.HiddenInput(),
        }

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'description', 'image')
        labels = {
        'title': 'Título',
        'description': 'Descripción',
        'image': 'Imagen'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }

        
