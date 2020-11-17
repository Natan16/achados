# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from core.service import log_svc, achados_svc
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from google.oauth2 import id_token
from google.auth.transport import requests

def dapau(request):
    raise Exception('break on purpose')

@csrf_exempt
def google_login(request):
    token = request.POST.get('id_token')
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),
                                              "649795675193-qiheujqkem1i9k0r7boqr0o0c9n5rk83.apps.googleusercontent.com"
                                              )
            
        #TODO se usuário não existir, criar ele
        #se já existir, mas ainda não foi logado com google, logar


        return JsonResponse({}, safe=False)

    except ValueError:
        # Invalid token
        pass



@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)

def adiciona_registro(request):
    registro = achados_svc.adiciona_registro(request.POST.get('solicitante_nome'),request.POST.get('solicitante_email'),
                                             request.POST.get('doc_tipo'),request.POST.get('doc_numero'),
                                             request.POST.get('doc_outro'),request.POST.get('doc_nome'),
                                             request.POST.get('tipo_reg'))
    #os métodos post tem que retornar uma resposta HTTP?
    return JsonResponse(registro)

def lista_correspondencias(request):
    correspondencias = achados_svc.lista_correspondencias(request.GET.get('doc_tipo'), request.GET.get('doc_numero'),
                                                          request.GET.get('doc_outro'),request.GET.get('doc_nome_prop'),
                                                          request.GET.get('tipo_reg'))

    return JsonResponse(correspondencias, safe=False)

#seria post, pois executa uma ação ou get, pois não altera o banco de dados?
def envia_email(request):
    result = send_mail(
        'Achados & Perdidos ',
        request.POST.get('texto'),
        'nao_tem@gmail.com',
        [request.POST.get('destinatario')],
        fail_silently=False,

    )
    #auth_user = 'EMAIL_AQUI',
    #auth_password = 'SENHA_AQUI'

    return HttpResponse('{}')

def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
