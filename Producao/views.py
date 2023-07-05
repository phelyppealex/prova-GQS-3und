from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm

@login_required
def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            criacao = form.cleaned_data['criacao']
            data = form.cleaned_data['data']
            quantidade = form.cleaned_data['quantidade']

            Coleta.objects.create(
                criacao=criacao,
                data=data,
                quantidade=quantidade
            )
            return redirect('Producao:listar_coletas')
    else:
        form = ColetaForm()

    informacoes = {
        'form': form
    }

    return render(request, 'Producao/criar_produto.html', informacoes)

