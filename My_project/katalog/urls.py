from django.urls import path
from . import views

urlpatterns = [

    path('', views.models_car, name='catalog'),

]