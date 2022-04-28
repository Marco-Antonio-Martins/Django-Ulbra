from django.contrib import admin
from django.urls import path
from app_noticias.views import resumo_pessoas, index

urlpatterns = [ #passar name=""
    path('', index, name="index"),
    path('pessoas/', resumo_pessoas, name="resumo_pessoas"),    
]
