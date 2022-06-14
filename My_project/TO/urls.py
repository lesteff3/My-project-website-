from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.register_on_to, name='register_on_to'),
    path('Successful_registration_on_to/', views.registers_person_on_to, name='register_person_on_to')



]