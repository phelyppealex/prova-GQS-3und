from django.test import TestCase
from unittest.mock import Mock
from Producao.models import Criacao, Coleta

class CriacaoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Apis mellifera', data_entrada='20/04/2023')
        Criacao.objects.create(raca='Apis mellifera mellifera', data_entrada='')
        Criacao.objects.create(raca='Apis mellifera ligustica', data_entrada='07/03/2022')
        Criacao.objects.create(raca='Caucasica', data_entrada='27/05/2021')
        Criacao.objects.create(raca='Apis mellifera carnica da Eslovênia', data_entrada='23/')
        Criacao.objects.create(raca='Apis mellifera scutellata', data_entrada='')

    def test_tamanho_caracteres(self):
        criacao = Criacao.objects.get(id=1)
        raca = criacao._meta.get_field('raca')
        tamanho_max = criacao._meta.get_field('raca').max_length
        self.assertTrue(len(raca) <= tamanho_max)

    def test_campos_obrigatorios(self):
        criacao = Criacao.objects.get(id=1)
        raca = criacao._meta.get_field('raca')
        data = criacao._meta.get_field('data_entrada')
        self.assertTrue(raca != None)
        self.assertTrue(data != None)

    def test_verbose_name(self):
        criacao = Criacao.objects.get(id=1)
        raca = criacao._meta.get_field('raca')
        data = criacao._meta.get_field('data_entrada')
        self.assertEqual(raca.verbose_name, 'raca')
        self.assertEqual(raca.verbose_name, 'data_entrada')

class ColetaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Coleta.objects.create(criacao='', data='20/04/2023', quantidade=3)
        Coleta.objects.create(criacao='', data='07/03/2022', quantidade=2)
        Coleta.objects.create(criacao='', data='27/05/2021', quantidade=5)
        Coleta.objects.create(criacao='', data='02/01/2023', quantidade=1)

        def test_tamanho_caracteres(self):
            coleta = Coleta.objects.get(id=1)
            data = coleta._meta.get_field('data')
            tamanho_max = coleta._meta.get_field('data').max_length
            self.assertTrue(len(data) <= tamanho_max)

        def test_campos_obrigatorios(self):
            coleta = Coleta.objects.get(id=1)
            data = coleta._meta.get_field('data')
            quantidade = coleta._meta.get_field('quantidade')
            self.assertTrue(data != None)
            self.assertTrue(quantidade != None)

        def test_verbose_name(self):
            coleta = Coleta.objects.get(id=1)
            criacao = coleta._meta.get_field('criacao')
            data = coleta._meta.get_field('data')
            quantidade = coleta._meta.get_field('quantidade')
            self.assertEqual(criacao.verbose_name, 'criacao')
            self.assertEqual(data.verbose_name, 'data')
            self.assertEqual(quantidade.verbose_name, 'quantidade')

        def test_ordem_coletas(self):
            coletas = Coleta.objects.order_by('-data')
            ordenado = checar_ordenacao_data(coletas)
            self.assertTrue(ordenado)

        def checar_ordenacao_data(coletas):
            ordenado = True
            i = 0
            while i < len(coletas) - 2:
                if coletas[i].data < coletas[i+1].data:
                    ordenado = False
                    break
            return ordenado