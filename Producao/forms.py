from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Producao.models import Coleta, Criacao

class ColetaForm(ModelForm):
    class Meta:
        model = Coleta
        fields = ['criacao', 'data', 'quantidade']

    def clean(self):
        cleaned_data = super().clean()

        criacao = self.cleaned_data['criacao']
        data = self.cleaned_data['data']
        quantidade = self.cleaned_data['quantidade']

        coletas_existentes = Coleta.objects.filter(criacao=criacao, data=data, quantidade=quantidade)

class CriacaoForm(ModelForm):
    class Meta:
        model = Criacao
        fields = ['raca', 'data_entrada']

    def clean(self):
        cleaned_data = super().clean()

        raca = self.cleaned_data['raca']
        data_entrada = self.cleaned_data['data_entrada']

        Criacao.objects.filter(raca=raca, data_entrada=data_entrada)