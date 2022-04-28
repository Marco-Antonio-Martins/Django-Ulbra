from django.shortcuts import render
from django.http import HttpResponse
from app_noticias.models import Pessoa

def resumo_pessoas(request):
    total = Pessoa.objects.count()
    return HttpResponse('O total de pessoas é: {}'.format(total))

def index(request):
    return HttpResponse('Bem vindo a nossa página')