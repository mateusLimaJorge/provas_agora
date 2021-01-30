from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"alunos", views.AlunosViewSet)
router.register(r"prova", views.AlunosViewSet)
router.register(r"perguntaprova", views.AlunosViewSet)
router.register(r"gabarito", views.AlunosViewSet)
router.register(r"respostagabarito", views.AlunosViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    ...
]