from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
...
from rest_framework import viewsets

from .models import Event, Comment
from .forms import EventForm, CommentForm
from .serializers import AlunosSerializer, ProvaSerializer, PerguntasProvaSerializer, GabaritoSerializer, RespostaGabaritoSerializer
...

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class_alunos = AlunosSerializer

class ProvaViewSet(viewsets.ModelViewSet):
    queryset = Provas.objects.all()
    #serializer_class_alunos = AlunosSerializer

class PerguntasProvaViewSet(viewsets.ModelViewSet):
    queryset = PerguntasProva.objects.all()
    # serializer_class_alunos = AlunosSerializer

class GabaritoViewSet(viewsets.ModelViewSet):
    queryset = Gabarito.objects.all()
    # serializer_class_alunos = AlunosSerializer

class RespostaGabaritoViewSet(viewsets.ModelViewSet):
    queryset = RespostaGabarito.objects.all()
    # serializer_class_alunos = AlunosSerializer