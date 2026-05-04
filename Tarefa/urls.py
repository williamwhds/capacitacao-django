from rest_framework.routers import DefaultRouter

from .views import TarefaModelViewSet

Trouter = DefaultRouter()
Trouter.register(r"Tarefa", TarefaModelViewSet, basename="Tarefa")

urlpatterns = Trouter.urls
