from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


title = 'Geely motors'

def index(request):
    context={
        'title': title
    }
    return render(request, 'home/index.html', context=context)


def about_company(request):
    return render(request, 'home/about.html', {'title': 'Контактная информация:'})



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')