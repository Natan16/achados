# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, achados_svc
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


def dapau(request):
    raise Exception('break on purpose')


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
    correspondencias = achados_svc.lista_correspondencias(request.GET['doc_tipo'], request.GET['doc_numero'], request.GET['doc_outro'],
                                       request.GET['doc_nome_prop'], request.GET['tipo_reg'] )

    return JsonResponse(correspondencias, safe=False)

#seria post, pois executa uma ação ou get, pois não altera o banco de dados?
def envia_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    JsonResponse({})

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
