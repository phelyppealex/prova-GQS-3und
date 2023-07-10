from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm, CriacaoForm

# Views de Coleta

def home(request):
    return render(request, 'Producao/index.html')

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
    return render(request, 'Producao/criar_coleta.html', informacoes)

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
    coleta = Coleta.objects.get(id=pk)
    informacoes = {
        'coleta': coleta
    }
    return render(request, 'Producao/detalhes_coleta.html', informacoes)

class DetalharColeta(DetailView):
    model = Coleta
    context_object_name = 'coleta'
    template_name = 'Producao/detalhes_coleta.html'

# Views de Criação

#@login_required
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

class CriarCriacao(CreateView):
    model = Criacao
    form_class = CriacaoForm
    template_name = 'Producao/criar_criacao.html'
    success_url = reverse_lazy('Producao:listar_coletar')

def listar_criacoes(request):
    lista_criacoes = Coleta.objects.all()

    informacoes = {
        'lista_criacoes': lista_criacoes
    }

    return render(request, 'Producao/listar_criacoes.html', informacoes)

class ListarCriacoes(ListView):
    model = Criacao
    context_object_name = 'lista_criacoes'
    template_name = 'Producao/listar_criacoes.html'

def detalhar_criacao(request, pk):
    criacao = Criacao.objects.get(id=pk)

    informacoes = {
        'criacao': criacao
    }

    return render(request, 'Producao/detalhes_criacao.html', informacoes)

class DetalharCriacao(DetailView):
    model = Criacao
    context_object_name = 'criacao'
    template_name = 'Producao/detalhes_criacao.html'