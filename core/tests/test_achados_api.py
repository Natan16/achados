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
        fixtures.usuario_natan()



    def test_registro_resultado(self):
        natan, anon= Client(), Client()
        natan.force_login(User.objects.get(username='Natan'))
        #usuário logado perde um documento
        self._regristra(natan,'Natan', 'natanvianat16@gmail.com', 'RA' , '585291', '','Natan Lima Viana' , 'perdido')
        self._assert_correspondencias(natan, 'RA', '585291', '', 'achado', 'Natan Lima Viana' , [] , [])

        #usuário não logado acha o documento
        self._regristra(anon,'Mariana', 'marianainaradacosta@gmail.com', 'RA' , '585291', '','Natan Lima Viana' , 'achado')
        self._assert_correspondencias(anon, 'RA' , '585291', '', 'perdido', 'Natan Lima Viana', ['Natan'], ['natanvianat16@gmail.com'])
        '''
        r = anon.post('/api/envia_email', {'destinatario': 'natanvianat16@gmail.com', 'texto':'Olá, Mariana achou o RG '
                                                                                                'que você registrou. '
                                                                                                'Envie um email para '
                                                                                               'marianainaradacosta@gmail.com'
                                                                                                ' para combinar os detablhes'                                                                                        ' da devolução'})
        self.assertEqual(200, r.status_code)
        '''

    def test_consulta_exclusao(self):
        natan = Client()
        natan.force_login(User.objects.get(username='Natan'))

        self._regristra(natan, 'Natan', 'natanvianat16@gmail.com', 'RA', '585291', '', 'Natan Lima Viana', 'perdido')
        self._regristra(natan, 'Natan', 'natanvianat16@gmail.com', 'Outro', '2222A', 'Clube Karate', 'João Silva', 'achado')
        self._regristra(natan, 'Natan', 'natanvianat16@gmail.com', 'RG', '1234', '', 'Natan Lima Viana', 'perdido')

        registros = self._assert_registros(natan, ['RA' , 'Clube Karate' , 'RG'] , ['585291','2222A','1234'])
        id_registro = [r['id'] for r in registros if r['tipo_doc']=='RA']
        self._exclui(natan, id_registro) #só a exclusão não funcionou, e isso e maravilhoso
        self._assert_registros(natan, ['Clube Karate', 'RG'], ['2222A', '1234'])

    def _regristra(self ,client , nome , email , tipo , numero , outro , nome_prop , tipo_reg):
        r = client.post('/api/adiciona_registro', {'solicitante_nome': nome, 'solicitante_email': email,
                                                    'doc_tipo': tipo, 'doc_numero': numero, 'doc_outro': outro,
                                                    'doc_nome': nome_prop, 'tipo_reg': tipo_reg})
        self.assertEqual(200, r.status_code)

    def _assert_correspondencias(self ,client,  tipo , numero, outro , tipo_reg , nome_prop , nomes_esperados ,
                                 emails_esperados):
        r = client.get('/api/lista_correspondencias', {'doc_tipo': tipo, 'doc_numero': numero, 'doc_outro': outro,
                                                        'tipo_reg': tipo_reg, 'doc_nome': nome_prop})
        self.assertEqual(200, r.status_code)
        correspondencias = json.loads(r.content.decode('utf-8'))
        nomes = [c['nome'] for c in correspondencias]
        emails = [c['email'] for c in correspondencias]
        self.assertEqual(nomes, nomes_esperados)
        self.assertEqual(emails, emails_esperados)

    def _assert_registros(self, client, tipos_esperados , numeros_esperados):
        r = client.get('/api/consulta_registros')
        self.assertEqual(200, r.status_code)
        registros = json.loads(r.content.decode('utf-8'))
        tipos = [r['tipo_doc'] for r in registros]
        numeros = [r['numero_doc'] for r in registros]
        self.assertEqual(tipos, tipos_esperados)
        self.assertEqual(numeros, numeros_esperados)
        return registros

    def _exclui(self , client , id_registro):
        r = client.post('/api/exclui_registro', {'id': id_registro})
        self.assertEqual(200, r.status_code)

    def test_autenticacao_google(self):
        pass





    def _assert_consulta(self):
        pass

    def _envia_email(self):
        pass
