from django.contrib import admin
from django.urls import path, include

urlpatterns = [ #passar name=""
    path('admin/', admin.site.urls),
    path('eventos/', include('app_noticias.urls')), #include manda para app_noticias_urls
]
