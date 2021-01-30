from rest_framework import serializers
from .models import Event

class AlunosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("nome")


class ProvaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("nome")

class PerguntasProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id_prova", "pergunta", "resposta")

class GabaritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id_prova","id_aluno")

class RespostaGabaritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id_gabarito", "id_pergunta", "resposta")