from django.urls import path
from .views import index, about_company


urlpatterns = [

    path('', index, name='index'),
    path('about/', about_company, name='about')

]
