from django.urls import path
from . import views

urlpatterns = [

    path('', views.models_car, name='catalog'),
    path('Atlas/', views.gelly_atlas, name='atlas'),
    path('Coolray/', views.gelly_coolray, name='coolray'),
    path('Emgrand/', views.gelly_emgrand, name='emgrand'),
    path('Atlas Pro/', views.gelly_atlas_pro, name='atlas-pro'),
    path('GS/', views.gelly_gs, name='gs'),
    path('Tugella/', views.gelly_tugella, name='tugella'),


]