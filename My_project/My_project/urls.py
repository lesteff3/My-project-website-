from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home_page.views import pageNotFound


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('news/', include('news.urls')),
    path('register/', include('register.urls')),
    path('catalog/', include('katalog.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = pageNotFound