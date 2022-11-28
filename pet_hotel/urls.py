from django.urls import include, path
from .views import pet_hotel, customers, admins

urlpatterns = [
    path('', pet_hotel.home, name='home'),
    path('service/', pet_hotel.service, name='service'),
    path('contact/', pet_hotel.contact, name='contact'),
    path('news/', pet_hotel.news, name='news'),

    path('customers/', include(([
        path('profile/', customers.ProfileCustomerView.as_view(), name='profile_customers'),
        path('news/', customers.news, name='news_customers'),
        path('service/', customers.service, name='service_customers'),
        path('deletepets/<int:pk>/', customers.delete_pets, name='delete_pets'),
        #path('appointment/', customers.ApointmentCustomerView.as_view(), name='appointment_customers'),
    ], 'pet_hotel'), namespace='customers')),

    path('admins/', include(([
        path('profile/', admins.ProfileAdminView.as_view(), name='profile_admins'),
        # path('contact/', admins.ContactAdminView.as_view(), name='contact_admins'),
        # path('news/', admins.NewsAdminView.as_view(), name='news_admins'),
        # path('service/', admins.ServiceAdminView.as_view(), name='service_admins'),
    ], 'pet_hotel'), namespace='admins')),
]