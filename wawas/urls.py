"""wawas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pet_hotel.views import pet_hotel, customers, admins
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pet_hotel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', pet_hotel.SignUpView.as_view(), name='signup'),
    path('accounts/signup/customers/', customers.CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/signup/admins/', admins.AdminSignUpView.as_view(), name='admin_signup'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
