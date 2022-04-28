from django.contrib import admin
from django.urls import path
from app_noticias.views import resumo_pessoas, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoas/', resumo_pessoas),
    path('', index)
]
