# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from core.service import log_svc, achados_svc
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from google.oauth2 import id_token
from google.auth.transport import requests
from commons.django_views_utils import ajax_login_required
from core.models import User
def dapau(request):
    raise Exception('break on purpose')

@csrf_exempt
def google_login(request):
    token = request.POST.get('id_token')
    try:
        #TODO por o CLIENT_ID num arquivo fora do git
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),
                                              "649795675193-qiheujqkem1i9k0r7boqr0o0c9n5rk83.apps.googleusercontent.com"
                                              )
        perfil = achados_svc.google_login(idinfo['email'],idinfo['name'],idinfo['picture'],idinfo['given_name'],
        idinfo['family_name'])

        #TODO na verdade pode usar o password hasherizado que a google manda
        usuario = auth.authenticate(username=perfil.usuario.username, password="abc12345")
        auth.login(request , usuario)
        if usuario is None :
            return JsonResponse({'usuario':'Nenhum'}, safe=False)
        return JsonResponse(perfil.to_dict_json(), safe=False)

    except ValueError:
        return JsonResponse(None, safe=False)


#nao vai ser mais chamado
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
    loggeduser = request.user if request.user.is_authenticated() else None

    registro = achados_svc.adiciona_registro(loggeduser, request.POST.get('solicitante_nome'),
                                             request.POST.get('solicitante_email'),
                                             request.POST.get('doc_tipo'), request.POST.get('doc_numero'),
                                             request.POST.get('doc_outro'), request.POST.get('doc_nome'),
                                             request.POST.get('tipo_reg'))
    return JsonResponse(registro, safe=False)

def lista_correspondencias(request):

    correspondencias = achados_svc.lista_correspondencias(request.GET.get('doc_tipo'), request.GET.get('doc_numero'),
                                                          request.GET.get('doc_outro'),request.GET.get('doc_nome'),
                                                          request.GET.get('tipo_reg'))

    return JsonResponse(correspondencias, safe=False)

@ajax_login_required
def consulta_registros(request):
    loggeduser = request.user
    registros = achados_svc.consulta_registros(loggeduser)
    return JsonResponse(registros, safe=False)

@ajax_login_required
def exclui_registro(request):
    achados_svc.exclui_registro(request.POST.get('id'))
    return JsonResponse({})

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
