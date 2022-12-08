from django.urls import include, path
from .views import pet_hotel, customers, admins

urlpatterns = [
    path('', pet_hotel.home, name='home'),
    path('service/', pet_hotel.service, name='service'),
    path('contact/', pet_hotel.contact, name='contact'),
    path('news/', pet_hotel.news, name='news'),
    path('createpublication/', pet_hotel.CreatePublicationView.as_view() , name='create_publication'),
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
        path('createpetwatcher/', customers.PetWatcherCreateView.as_view(), name='petwatcher_create'),
        path('cuidadoreslist/', customers.customer_is_dog_watcher, name='petwatcher_list'),
        # path('sendmessage/<int:pk>/', customers.send_message, name='send_message'),
        path('inbox/', customers.ListThreads.as_view(), name='inbox'),
        path('inbox/create-thread/<int:pk>/', customers.CreateThread.as_view(), name='create-thread'),
        path('inbox/<int:pk>/', customers.ThreadView.as_view(), name='thread'),
        path('inbox/<int:pk>/create-message/', customers.CreateMessage.as_view(), name='create-message'),
    ], 'pet_hotel'), namespace='customers')),

    path('admins/', include(([
        path('profile/', admins.UserListView.as_view(), name='profile_admins'),
        path('edituser/<int:pk>/', admins.edit_status, name='edit_status'),
        path('service/', admins.ServiceListView.as_view(), name='service_admins'),
        path('apointmetcheck/<int:pk>/', admins.AppointmentCheckView.as_view(), name='appointment_check'),
        path('appointmentchangestatus/<int:pk>/<str:type>/', admins.change_status, name='appointment_change_status'),
        path('appointmentedit/<int:pk>/', admins.update_appointment, name='appointment_edit'),
        path('appointmentdelete/<int:pk>/', admins.delete_appointment, name='appointment_delete'),
        path('petwatchercheck/<int:pk>/', admins.PetWatcherCheckView.as_view(), name='petwatcher_check'),
        path('petwatcherdelete/<int:pk>/', admins.delete_petwatcher, name='petwatcher_delete'),
        path('customerisdogwatcher/<int:pk>/', admins.customer_is_dog_watcher, name='customer_is_dog_watcher'),
    ], 'pet_hotel'), namespace='admins')),
]