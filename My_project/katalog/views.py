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


def gelly_atlas(request):
    name ={
        'title': 'Gelly Atlas'
    }
    return render(request, 'Geely Atlas.html', name)


def gelly_atlas_pro(request):
    name = {
        'title': 'Gelly Atlas PRO'
    }
    return render(request, 'Atlas Pro.html', name)


def gelly_emgrand(request):
    name = {
        'title': 'Gelly Emgrand'
    }
    return render(request, 'Emgrand.html', name)


def gelly_gs(request):
    name = {
        'title': 'Gelly GS'
    }
    return render(request, 'Geely GS.html', name)


def gelly_tugella(request):
    name = {
        'title': 'Gelly Tugella'
    }
    return render(request, 'Tugella.html', name)


def gelly_coolray(request):
    name = {
        'title': 'Gelly Coolray'
    }
    return render(request, 'Coolray.html', name)


