from django.db import IntegrityError
from core.models import Documento, Registro, User, Profile
from django.db.models import Q
from commons.utils import gravatar_url

def google_login(email,name,picture,given_name,family_name):
    #Profile.objects.all().delete()
    perfil , _ = Profile.objects.get_or_create(email=email) #as vezes está retornando mais do que 1 perfil, por que?
    if (not perfil.usuario):
        try:
            perfil.usuario = User.objects.create_user(username=name, email=email, password="abc12345",
                                           first_name=given_name, last_name=family_name)

        except IntegrityError:
            perfil.usuario = User.objects.get(username=name, email=email)
        perfil.avatar = picture
        perfil.nome = given_name
        perfil.save()
    return perfil

def adiciona_registro(loggeduser, solicitante_nome, solicitande_email, doc_tipo,
                      doc_numero, doc_outro, doc_nome, tipo_reg):
    try :
        usuario = User.objects.get(email=solicitande_email)
    except:
        usuario = None

    if (usuario and not loggeduser) or (loggeduser and loggeduser.email != solicitande_email):
        return None
    if (not loggeduser):
        perfil,criado = Profile.objects.get_or_create(email=solicitande_email)
        if perfil.usuario:
            return None #usuário não logado não adicionar registro como usuário logado
        elif criado:
            avatar = gravatar_url(solicitande_email)
            perfil.avatar = avatar
            perfil.save()

    else:
        perfil = Profile.objects.get(email=solicitande_email)

    perfil.nome = solicitante_nome
    perfil.save()

    outro = True if doc_tipo == 'Outro' else False
    doc_tipo = doc_outro if outro else doc_tipo

    documento , _ = Documento.objects.get_or_create(tipo=doc_tipo, outro=outro, numero=doc_numero,
                                         nomeProprietario=doc_nome)

    registro = Registro.objects.create(profile=perfil, documento=documento, tipoRegistro=tipo_reg)

    return registro.to_dict_json()


def lista_correspondencias(doc_tipo , doc_numero , doc_outro ,
                                       doc_nome , tipo_reg):
    outro = True if doc_tipo == 'Outro' else False
    doc_tipo = doc_outro if outro else doc_tipo

    registros = Registro.objects.filter(
        Q(documento__in=Documento.objects.filter(tipo=doc_tipo, outro=outro, numero=doc_numero)) &
        Q(tipoRegistro=tipo_reg))

    return [r.to_dict_json() for r in registros]

def consulta_registros(loggedUser):
    registros =  Registro.objects.filter(
        Q(profile__in=Profile.objects.filter(usuario=loggedUser)))
    return [r.to_dict_json() for r in registros]

def exclui_registro(id):
    Registro.objects.filter(id=id).delete()

def toggle_status(id):
    registro = Registro.objects.get(id=id)
    registro.status = 0 if registro.status == 1 else 1
    registro.save()