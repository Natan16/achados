from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestAchadosApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()

    def test_achados_api(self):
        client = Client()

        # r1 = client.get('/api/whoami')
        # client.force_login(User.objects.get(username='jon'))
        # r2 = client.post('/api/login', {'username': 'jon', 'password': 'snow'})
        # r3 = client.get('/api/whoami')
        # r4 = client.post('/api/logout')
        # r5 = client.get('/api/whoami')
        #criar formularios padrao pra testar as possiveis respostas da api no preenchimento
        #pex : com ou sem o tipo outro, com nome de usuario valido etc
        r1 = client.get('api/adiciona_registro', {'' : ' ', '' : ' '})
        r2 = client.post('api/lista_correspondencias', {'' : ' ', '' : ' '})
        self.assertEqual(200, r1.status_code)
        self.assertEqual(200, r2.status_code)
        # faz um assert se as correspondencias são o esperado
        # manda os emails para as correspondencias
        # faz assert de OK da requisição
        info = json.loads(r1.content.decode('utf-8'))
