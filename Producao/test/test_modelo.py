from django.test import TestCase
from unittest.mock import Mock
from Producao.models import Criacao, Coleta

class CriacaoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Apis mellifera', data_entrada='2023-04-20')
        Criacao.objects.create(raca='Apis mellifera mellifera', data_entrada='2020-11-22')
        Criacao.objects.create(raca='Apis mellifera ligustica', data_entrada='2022-03-07')
        Criacao.objects.create(raca='Caucasica', data_entrada='2021-05-27')
        Criacao.objects.create(raca='Apis mellifera carnica da Eslovênia', data_entrada='2023-01-11')
        Criacao.objects.create(raca='Apis mellifera scutellata', data_entrada='2019-03-11')

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
        self.assertEqual(data.verbose_name, 'data_entrada')

class ColetaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Criacao.objects.create(raca='Apis mellifera', data_entrada='2023-04-20')
        Criacao.objects.create(raca='Apis mellifera mellifera', data_entrada='2020-11-22')
        Criacao.objects.create(raca='Apis mellifera ligustica', data_entrada='2022-03-07')
        Criacao.objects.create(raca='Caucasica', data_entrada='2021-05-27')
        Criacao.objects.create(raca='Apis mellifera carnica da Eslovênia', data_entrada='2023-01-11')
        Criacao.objects.create(raca='Apis mellifera scutellata', data_entrada='2019-03-11')

        Coleta.objects.create(criacao=Criacao.objects.get(id=1), data='2023-04-20', quantidade=3)
        Coleta.objects.create(criacao=Criacao.objects.get(id=3), data='2022-03-07', quantidade=2)
        Coleta.objects.create(criacao=Criacao.objects.get(id=1), data='2021-05-27', quantidade=5)
        Coleta.objects.create(criacao=Criacao.objects.get(id=2), data='2023-01-02', quantidade=1)

        def test_tamanho_caracteres(self):
            coleta = Coleta.objects.get(id=1)
            data = coleta._meta.get_field('data')
            tamanho_max = coleta._meta.get_field('data').max_length
            self.assertTrue(data.max_length <= tamanho_max)

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