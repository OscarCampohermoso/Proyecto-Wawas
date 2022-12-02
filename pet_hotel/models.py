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
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    is_dog_watcher = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Contact (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    message=models.CharField(max_length=600)

    def __str__(self):     
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    breed = models.CharField(max_length=200, blank=True)
    size = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='pet_images', blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    request = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    date_of_request = models.DateField(auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=True)
    status = models.CharField(max_length=200, blank=True, default='Pendiente')

    def __str__(self):
        return self.type

class Publication(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='publication_images', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

class PetWatcher(models.Model):
    reason = models.CharField(max_length=200, blank=True, null=False)
    accept = models.BooleanField(blank=True, null=False)
    photo = models.ImageField(upload_to='pet_watcher_images', blank=True, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.reason


