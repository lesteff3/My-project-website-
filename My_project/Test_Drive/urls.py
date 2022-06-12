from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.register_on_test_drive, name='register_on_test_drive'),
    path('Successful_registration/', views.registers_person, name='register_person')



]