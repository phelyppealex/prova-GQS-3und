from django.contrib import admin

# Register your models here.
from Producao.models import Criacao, Coleta

admin.site.register(Criacao)
admin.site.register(Coleta)