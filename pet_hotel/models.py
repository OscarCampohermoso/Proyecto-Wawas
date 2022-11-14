from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Contact (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=320)
    phone=models.PositiveIntegerField()
    message=models.CharField(max_length=600)

    def __str__(self):
        texto = "Name: {0} Email: {1} Phone: {2} Message: {3}"        
        return texto.format(self.name, self.email, self.phone, self.message)


