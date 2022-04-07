from django.contrib import admin
from .models import Noticia, Pessoa, Tag

# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass