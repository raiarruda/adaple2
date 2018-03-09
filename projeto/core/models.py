from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class db_habilidades (models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class db_edp(models.Model):
    
    nome = models.CharField(max_length=100)
    objetivo_pedagogigo = models.TextField()
    habilidades = models.ManyToManyField(db_habilidades)
    atividades = models.TextField()
    metodologia = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING,)

    def iniciar(self):
        self.save()

    def __str__(self):
        return self.nome


class db_recursos (models.Model):
    edp = models.ForeignKey(db_edp, on_delete=models.CASCADE)
    video = EmbedVideoField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    player_audio = models.NullBooleanField(blank=True, null=True)
    player_imagem = models.NullBooleanField(blank=True, null=True)

    def iniciar(self):
        self.save()

    def __str__ (self):
        return self.edp.nome

class db_edp_aluno(models.Model):

    aluno = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    edp = models.ForeignKey(db_edp, on_delete=models.CASCADE, null=True)
    resposta = models.TextField(blank=True, null=True)
    resposta_video = EmbedVideoField(blank=True, null=True)
  
    def iniciar(self):
        self.save
    
    def __str__(self):
        return self.aluno.username


#

