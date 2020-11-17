from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json

TEXTO_EMAIL = '%s alega ter encontrado seu %s entre em contato com ele através do' \
                'email %s para combinarem a devolução.'

class TestAchadosApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()

    def test_achados_api(self):
        client = Client()
        # pessoa perde um documento
        #force login?
        r1 = client.post('/api/adiciona_registro', {'solicitante_nome': 'Natan', 'solicitante_email': 'natan@gmail.com',
                                        'doc_tipo': 'RA', 'doc_numero': '585291', 'doc_outro': '',
                                        'doc_nome': 'Natan Lima Viana', 'tipo_reg': 'perdido'})
        self.assertEqual(200, r1.status_code)
        r2 = client.get('/api/lista_correspondencias', {'doc_tipo': 'RA', 'doc_numero': '585291', 'doc_outro': '',
                                                       'tipo_reg': 'achado', 'doc_nome':'Natan Lima Viana'})
        #nenhuma correspondencia é encontrada
        self.assertEqual(200, r2.status_code)
        correspondencias = json.loads(r2.content.decode('utf-8'))
        nomes = [c['nome'] for c in correspondencias]
        emails = [c['email'] for c in correspondencias]
        self.assertEqual(nomes, [])
        self.assertEqual(emails, [])

        # pessoa acha um documento
        r3 = client.post('/api/adiciona_registro', {'solicitante_nome': 'Mariana',
                                        'solicitante_email': 'marianainaradacosta@gmail.com',
                                        'doc_tipo': 'RA', 'doc_numero': '585291', 'doc_outro': '',
                                        'doc_nome': 'Natan Lima Viana', 'tipo_reg': 'achado'})
        self.assertEqual(200, r3.status_code)
        r4 = client.get('/api/lista_correspondencias', {'doc_tipo': 'RA', 'doc_numero': '585291', 'doc_outro': '',
                                                       'tipo_reg': 'perdido', 'doc_nome':'Natan Lima Viana'})
        self.assertEqual(200, r4.status_code)
        #correspondencia é encontrada
        correspondencias = json.loads(r4.content.decode('utf-8'))
        nomes = [c['nome_solicitante'] for c in correspondencias]
        emails = [c['email_solicitante'] for c in correspondencias]
        self.assertEqual(nomes, ['Natan'])
        self.assertEqual(emails, ['natan@gmail.com'])
        #email é enviado para a pessoa que perdeu
        nome = nomes[0]
        email = emails[0]

        r5 = client.post('/api/envia_email', {'destinatario': 'natanvianat16@gmail.com', 'texto':'Olá, Mariana achou o RG '
                                                                                                'que você registrou. '
                                                                                                'Envie um email para '
                                                                                                'marianainaradacosta@gmail.com'
                                                                                                ' para combinar os detablhes'
                                                                                                ' da devolução'})
        self.assertEqual(200, r5.status_code)

    def test_autenticacao_google(self):
        client = Client()
        # pessoa perde um documento
        # force login?
        r1 = client.post('/api/adiciona_registro', {'solicitante_nome': 'Natan', 'solicitante_email': 'natan@gmail.com',
                                                    'doc_tipo': 'RG', 'doc_numero': '1234', 'doc_outro': '',
                                                    'doc_nome': 'Natan Lima Viana', 'tipo_reg': 'perdido'})

        self.assertEqual(200, r1.status_code)
        r2 = client.get('/api/lista_correspondencias', {'doc_tipo': 'RG', 'doc_numero': '1234', 'doc_outro': '',
                                                        'tipo_reg': 'achado', 'doc_nome': 'Natan Lima Viana'})
        self.assertEqual(200, r2.status_code)


    def _regristra(self):
        pass

    def _assert_correspondencias(self):
        pass

    def _assert_consulta(self):
        pass

    def _envia_email(self):
        pass
