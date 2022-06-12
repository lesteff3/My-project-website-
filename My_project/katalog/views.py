from django.shortcuts import render

# Create your views here.
from .models import Models_car


def models_car(request):
    models = Models_car.objects.all()
    context = {
        'title': 'Каталог',
        'models': models
    }
    return render(request, 'catalog.html', context=context)
