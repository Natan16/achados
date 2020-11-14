from core.models import Documento, Registro , User
from django.db.models import Q


def adiciona_registro(solicitante_nome, solicitande_email, doc_tipo,
    doc_numero, doc_outro, doc_nome_prop, tipo_reg):
    usuario = User.objects.create_user(solicitante_nome, solicitande_email, '' )
    documento = Documento.objects.create(tipo=doc_tipo, outro=doc_outro, numero=doc_numero,
                                         nomeProprietario=doc_nome_prop)
    registro = Registro.objects.create(usuario=usuario, documento=documento, tigoRegistro=tipo_reg)
    return usuario , documento , registro

def lista_correspondencias():
    #tem que fazer query considerando todas as possíveis variações para os parâmetros do documento
    pass
