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

#ver se user já não tem um campo equivalente à possui_login

class Documento(models.Model):
    tipo = models.TextField()  #tipos fixos ( seria melhor usar um enum ? já que o banco de dados não precisa saber o tipo)
    outro = models.TextField()
    numero =  models.TextField() #nao necessarimente eh um numero
    nomeProprietario = models.TextField()
    #proprietario = models.ForeignKey(User, null=True, empty=True )
    class Meta:
        unique_together = ('tipo', 'numero', 'outro')

#registros são únicos
class Registro(models.Model):
    usuario = models.ForeignKey(User)
    #se o registro for de documento perdido, pode até relacionar usuário à documento
    documento = models.ForeignKey(Documento)
    tipoRegistro = models.TextField()
    criado_em = models.DateTimeField('criado em', auto_now_add=True)
    status = models.SmallIntegerField(default=0)


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }
