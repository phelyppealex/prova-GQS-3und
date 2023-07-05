from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Producao.models import Coleta

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