from django.db import IntegrityError
from core.models import Documento, Registro, User, Profile
from django.db.models import Q
from commons.utils import gravatar_url

def google_login(email,name,picture,given_name,family_name):

    perfil,_ = Profile.objects.get_or_create(email=email)

    if (not perfil.usuario):
        try:
            perfil.usuario = User.objects.create_user(username=name, email=email,
                                           first_name=given_name, last_name=family_name)

        except IntegrityError:
            perfil.usuario = User.objects.get(username=name, email=email)
        perfil.avatar = picture
        perfil.nome = given_name
        perfil.save()
    return perfil.to_dict_json()

def adiciona_registro(loggeduser, solicitante_nome, solicitande_email, doc_tipo,
                      doc_numero, doc_outro, doc_nome, tipo_reg):
    #try :
       #usuario = User.objects.get(email=solicitande_email)
    #except:
    usuario = None

    if (usuario and not loggeduser) or (loggeduser and loggeduser.email != solicitande_email):
        return None
    if (not loggeduser):

       perfil,_ = Profile.objects.get_or_create(usuario=None, avatar="gravatar_url(solicitande_email)",
                              email=solicitande_email)
       perfil.nome = solicitante_nome
       perfil.save()
    else:
        perfil = Profile.objects.get(email=solicitande_email)
    print(perfil)
    perfil,_ = Profile.objects.get_or_create(usuario=None, avatar=gravatar_url(solicitande_email),
                              email=solicitande_email)
    perfil.nome = solicitante_nome
    perfil.save()
    #nome_parts = solicitante_nome.split()
    #nome = nome_parts[0]
    #sobrenome = " ".join(nome_parts[1:len(nome_parts)]) if len(nome_parts) > 1 else ""
    #Não vai mais criar usuário
    #try:
    #    usuario = User.objects.create_user(username=solicitande_email, email=solicitande_email,
    #                                       first_name=nome, last_name=sobrenome)
    #except IntegrityError:
    #    usuario = User.objects.get(username=solicitande_email, email=solicitande_email)

    outro = True if doc_tipo == 'Outro' else False
    doc_tipo = doc_outro if outro else doc_tipo

    documento , _ = Documento.objects.get_or_create(tipo=doc_tipo, outro=outro, numero=doc_numero,
                                         nomeProprietario=doc_nome)

    registro = Registro.objects.create(profile=perfil ,documento=documento, tipoRegistro=tipo_reg)

    return registro.to_dict_json()


#só está chegando aqui quando é usuário registrado ... problema é que não tem perfil associado ao registro
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
        Q(perfil__in=Profile.objects.filter(usuario=loggedUser)))

    return [r.to_dict_json() for r in registros]
