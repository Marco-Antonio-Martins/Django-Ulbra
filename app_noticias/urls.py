from django.contrib import admin
from django.urls import path
from app_noticias.views import resumo_pessoas, index, app_noticias_resumos_template, noticia_detalhes

urlpatterns = [ #passar name=""
    path('', index, name="index"),
    path('pessoas/', resumo_pessoas, name="resumo_pessoas"), 
    path('resumo/', app_noticias_resumos_template),   
    path('noticias/<int:noticia_id>/', noticia_detalhes, name='detalhes'),
]
