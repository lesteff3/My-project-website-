from django.shortcuts import render
from .models import News


def news(request):
    news = News.objects.order_by('data')
    context = {
        'title': 'Новости',
        'news': news
    }
    return render(request, 'news/news.html', context=context)
