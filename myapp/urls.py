from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add/', views.add_destination, name='add_destination'),
    path('destinations/<int:id>/', views.destination_detail, name='destination_detail'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('destinations/<int:destination_id>/appointments/new/', views.create_appointment, name='create_appointment'),
    path('appointments/<int:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),
    path('destinations/<int:destination_id>/edit/', views.edit_destination, name='edit_destination'),
]
