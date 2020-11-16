from django.db import IntegrityError

from core.models import Documento, Registro , User
from django.db.models import Q


def adiciona_registro(solicitante_nome, solicitande_email, doc_tipo,
                      doc_numero, doc_outro, doc_nome, tipo_reg):


    outro = True if doc_tipo == 'Outro' else False
    doc_tipo = doc_outro if outro else doc_tipo

    nome_parts = solicitante_nome.split()
    nome = nome_parts[0]
    sobrenome = " ".join(nome_parts[1:len(nome_parts)]) if len(nome_parts) > 1 else ""

    try:
        # usuário não autenticado tem foo como password
        usuario = User.objects.create_user(username=solicitande_email, email=solicitande_email, password='foo',
                                           first_name=nome, last_name=sobrenome)
    except IntegrityError:
        usuario = User.objects.get(username=solicitande_email, email=solicitande_email)

    documento , _ = Documento.objects.get_or_create(tipo=doc_tipo, outro=outro, numero=doc_numero,
                                         nomeProprietario=doc_nome)

    #tem que apagar o banco, pois essa query está retornando mais de 1 documento
    registro = Registro.objects.create(usuario=usuario, documento=documento, tipoRegistro=tipo_reg)
    return registro.to_dict_json()

def lista_correspondencias(doc_tipo , doc_numero , doc_outro ,
                                       doc_nome_prop , tipo_reg):
    outro = True if doc_tipo == 'Outro' else False
    doc_tipo = doc_outro if outro else doc_tipo

    registros = Registro.objects.filter(
        Q(documento__in=Documento.objects.filter(tipo=doc_tipo, outro=outro, numero=doc_numero)) &
        Q(tipoRegistro=tipo_reg))

    return [r.to_dict_json() for r in registros]
