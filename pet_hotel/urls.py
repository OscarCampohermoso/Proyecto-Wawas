from django.urls import include, path
from .views import pet_hotel, customers, admins

urlpatterns = [
    path('', pet_hotel.home, name='home'),
    path('service/', pet_hotel.service, name='service'),
    path('contact/', pet_hotel.contact, name='contact'),
    path('news/', pet_hotel.news, name='news'),
    path('createpublication/', pet_hotel.create_publication , name='create_publication'),
    path('updatepublication/<int:id>/', pet_hotel.update_publication , name='update_publication'),
    path('deletepublication/<int:id>/', pet_hotel.delete_publication , name='delete_publication'),

    path('customers/', include(([
        path('profile/', customers.ProfileCustomerView.as_view(), name='profile_customers'),
        path('service/', customers.service, name='service_customers'),
        path('deletepets/<int:pk>/', customers.delete_pets, name='delete_pets'),
        path('createpets/', customers.PetCreateView.as_view(), name='create_pets'),
        path('updatepets/<int:pk>/', customers.PetUpdateView.as_view(), name='update_pets'),
        path('appointment/<str:type>/', customers.appointment, name='appointment_customers'),
        path('apointmetcheck/<int:pk>/', customers.AppointmentCheckView.as_view(), name='appointment_check'),
        path('appointmentdelete/<int:pk>/', customers.delete_appointment, name='appointment_delete'),
    ], 'pet_hotel'), namespace='customers')),

    path('admins/', include(([
        path('profile/', admins.UserListView.as_view(), name='profile_admins'),
        path('edituser/<int:pk>/', admins.edit_status, name='edit_status'),
        path('service/', admins.ServiceListView.as_view(), name='service_admins'),
        path('apointmetcheck/<int:pk>/', admins.AppointmentCheckView.as_view(), name='appointment_check'),
    ], 'pet_hotel'), namespace='admins')),
]