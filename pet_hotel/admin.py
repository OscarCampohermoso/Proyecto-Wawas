from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import escape, mark_safe
from .models import User, Customer, Admin, Pet, Appointment, Publication, PetWatcher
from .models import Customer
# Add pet_hotel.User to the admin interface


admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Appointment)
admin.site.register(Publication)
admin.site.register(PetWatcher)


