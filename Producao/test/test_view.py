from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Producao.models import Coleta, Criacao
from Producao import views

class ColetaViewTest(TestCase):
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

    def setUp(self):
        usuario = User.objects.create_user(username='user0', password='123')
        usuario.save()

    def test_listar_criacao_url(self):
        response = self.client.get(reverse('listar_criacoes'))
        self.assertEquals(response.status_code, 200)

    def test_listar_criacao_template(self):
        response = self.client.get(reverse('listar_criacoes'))
        self.assertTemplateUsed(response, 'Producao/listar_criacoes.html')

    def test_criar_criacao_template(self):
        response = self.client.get(reverse('criar_criacao'))
        self.assertTemplateUsed(response, 'Producao/criar_criacao.html')

    def test_listar_criacao_all(self):
        response = self.client.get(reverse('listar_criacoes'))
        self.assertEqual(len(response.context['lista_criacoes']), 6)
    
    def test_listar_coleta_url(self):
        response = self.client.get(reverse('listar_coletas'))
        self.assertEquals(response.status_code, 200)

    def test_listar_coleta_template(self):
        response = self.client.get(reverse('listar_coletas'))
        self.assertTemplateUsed(response, 'Producao/listar_coletas.html')

    def test_criar_coleta_template(self):
        response = self.client.get(reverse('criar_coleta'))
        self.assertTemplateUsed(response, 'Producao/criar_coleta.html')

    """def test_detalhar_coleta_template(self):
        response = self.client.get(reverse('detalhes_coleta/<int:pk>)'))
        self.assertTemplateUsed(response, 'Producao/detalhes_coleta.html')"""

    def test_listar_coleta_all(self):
        response = self.client.get(reverse('listar_coletas'))
        self.assertEqual(len(response.context['lista_coletas']), 4)

    """def test_criar_coleta_redirect_login(self):
        response = self.client.get(reverse('Producao:criar_coletas'))
        self.assertRedirects(response, '/Producao/listar_coletas/?next=/produto/criar_coletas/')"""