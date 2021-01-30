# -*- coding: utf-8 -*-
from django.db import models

class Aluno(models.Model):
    class Meta:
        verbose_name = "Alunos"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome", default="", blank=True, db_index=True)

    def __str__(self):
        return self.description

class Prova(models.Model):
    class Meta:
        verbose_name = "Provas"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    nome = models.CharField(max_length=50, verbose_name="Nome", default="", blank=True, db_index=True)

    def __str__(self):
        return self.description

class PerguntasProva(models.Model):
    class Meta:
        verbose_name = "PerguntasProva"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    id_prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    descricao_pergunta = models.CharField(max_length=50, verbose_name="Descrição pergunta", default="", blank=True)
    resposta_correta = models.IntegerField(verbose_name='Resposta correta', default=None)

    def __str__(self):
        return self.description


class Gabarito(models.Model):
    class Meta:
        verbose_name = "Gabarito"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    id_prova = models.ForeignKey(Prova, verbose_name='Id Prova', on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, verbose_name='Id Aluno', on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class RespostaGabarito(models.Model):
    class Meta:
        verbose_name = "RespostaGabarito"

    objects = models.Manager()

    id = models.IntegerField(verbose_name='Id', serialize=False, primary_key=True, editable=False)
    id_pergunta_prova = models.ForeignKey(PerguntasProva, verbose_name='Id pergunta prova', on_delete=models.CASCADE)
    resposta = models.IntegerField(verbose_name='Resposta', default=None)

    def __str__(self):
        return self.description