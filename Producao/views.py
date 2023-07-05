from django.shortcuts import render, redirect
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm, CriacaoForm

# Views de Coleta

#@login_required
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

class CriarColeta(CreateView):
    model = Coleta
    form_class = ColetaForm
    template_name = 'Producao/criar_coleta.html'
    success_url = reverse_lazy('Producao:listar_coletas')

def listar_coletas(request):
    lista_coletas = Coleta.objects.all()

    informacoes = {
        'lista_coletas': lista_coletas
    }

    return render(request, 'Producao/listar_coletas.html', informacoes)

class ListarColetas(ListView):
    model = Coleta
    context_object_name = 'lista_coletas'
    template_name = 'Producao/listar_coletas.html'

def detalhar_coleta(request, pk):
    coleta = Coleta.objects.get(pk=pk)
    informacoes = {
        'coleta': coleta
    }
    return render(request, 'Producao/detalhes_coleta.html', informacoes)

class DetalharColeta(DetailView):
    model = Coleta
    context_object_name = 'coleta'
    template_name = 'Producao/detalhes_coleta.html'

# Views de Criação

def criar_criacao(request):
    if request.method == 'POST':
        form = CriacaoForm(request.POST)
        if form.is_valid():
            raca = form.cleaned_data['raca']
            data_entrada = form.cleaned_data['data_entrada']

            Criacao.objects.create(
                raca=raca,
                data_entrada=data_entrada
            )
            return redirect('Producao:listar_criacoes')
    else:
        form = CriacaoForm()

    informacoes = {
        'form': form
    }
    return render(request, 'Producao/criar_criacao.html', informacoes)