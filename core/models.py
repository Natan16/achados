from django.db import models
from django.contrib.auth.models import User


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Perfil(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    avatar = models.URLField()
    nome = models.TextField()
    email = models.EmailField()

    def to_dict_json(self):
        return {
            'username': self.nome,
            'first_name': self.usuario.first_name,
            'last_name': self.usuario.last_name,
            'email': self.numero,
            'avatar': self.avatar
        }


class Profile(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    avatar = models.URLField()
    nome = models.TextField()
    email = models.EmailField()

    def to_dict_json(self):
        return {
            'username': self.nome,
            'first_name': self.usuario.first_name,
            'last_name': self.usuario.last_name,
            'email': self.email,
            'avatar': self.avatar
        }

#possivel solução é fazer nova migração sem o perfil
class Documento(models.Model):
    tipo = models.TextField()
    outro = models.BooleanField()
    numero = models.TextField() #nao necessarimente eh um numero
    nomeProprietario = models.TextField()
    class Meta:
        unique_together = ('tipo', 'numero', 'outro')

    def to_dict_json(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'outro': self.outro,
            'numero': self.numero,
            'nomeProprietario': self.nomeProprietario
        }
#core registro nao possui perfil id
#registros são únicos
class Registro(models.Model):
    profile = models.ForeignKey(Profile, null=True)
    documento = models.ForeignKey(Documento)
    tipoRegistro = models.TextField()
    criado_em = models.DateTimeField('criado em', auto_now_add=True)
    status = models.SmallIntegerField(default=0)

    def to_dict_json(self):

        return {
            'nome':self.profile.nome,
            'email': self.profile.email,
            'avatar': self.profile.avatar,
            'tipo_doc': self.documento.tipo,
            'outro_doc': self.documento.outro,
            'numero_doc': self.documento.numero,
            'nomeProprietario_doc': self.documento.nomeProprietario,
            'criado_em': self.criado_em,
            'status': self.status,
            'tipo_reg': self.tipoRegistro
        }

class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }
