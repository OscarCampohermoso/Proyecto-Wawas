from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import escape, mark_safe

from .models import User, Customer

from .models import Customer

admin.site.register(Customer)

# if is_admin site register
admin.site.register(User, UserAdmin)

