from django.shortcuts import render
from django.http import HttpResponse
from app_noticias.models import Pessoa, Noticia

def resumo_pessoas(request):
    total = Pessoa.objects.count()
    return HttpResponse('O total de pessoas é: {}'.format(total))

def index(request):
    return HttpResponse('Bem vindo a nossa página')

def app_noticias_resumos_template(request):
    total = Pessoa.objects.count()
    return render(request, 'app_noticias/resumo.html', {'total_pessoas': total})

def noticia_detalhes(request, noticia_id):
    try: 
        noticia = Noticia.objects.get(pk=noticia_id)
    except Noticia.DoesNotExist:
        raise Http404('Notícia não encontrada')
    return render(request, 'app_noticias/detalhes.html', {'noticia': noticia})