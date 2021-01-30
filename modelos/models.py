from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models

class aluno(models.Model):
    class Meta:
        app_label = "aluno"
        verbose_name = "aluno"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome", default="", blank=True, db_index=True)

    def __str__(self):
        return self.description

class prova(models.Model):
    class Meta:
        app_label = "prova"
        verbose_name = "prova"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome", default="", blank=True, db_index=True)

    def __str__(self):
        return self.description

class perguntasprova(models.Model):
    class Meta:
        app_label = "perguntasprova"
        verbose_name = "perguntasprova"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    id_prova = models.ForeignKey(prova, on_delete=models.CASCADE)
    descricao_pergunta = models.CharField(max_length=50, verbose_name="Descrição pergunta", default="", blank=True)
    resposta_correta = models.IntegerField(verbose_name='Resposta correta', default=None)

    def __str__(self):
        return self.description


class gabarito(models.Model):
    class Meta:
        app_label = "gabarito"
        verbose_name = "gabarito"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    id_prova = models.ForeignKey(prova, verbose_name='Id Prova', on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(aluno, verbose_name='Id Aluno', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class respostagabarito(models.Model):
    class Meta:
        app_label = "respostagabarito"
        verbose_name = "respostagabarito"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    id_pergunta_prova = models.ForeignKey(perguntasprova, verbose_name='Id pergunta prova', on_delete=models.CASCADE)
    resposta = models.IntegerField(verbose_name='Resposta', default=None)

    def __str__(self):
        return self.description