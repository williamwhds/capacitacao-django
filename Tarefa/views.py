# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Usuario.models import Usuario

from .models import Tarefa
from .serializer import TarefaSerializer


class TarefaModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TarefaSerializer
    queryset = Tarefa.objects.all()

    def list(self, request):
        taf = Tarefa.objects.all()
        serial = TarefaSerializer(taf, many=True)
        if len(serial.data) > 0:
            return Response({"status": 302, "Tarefa": serial.data})
        return Response({"status": 204, "msg": "No Content"})

    @action(methods=["get"], detail=False)
    def TafOrder(self, request):
        Us = Usuario.objects.get(Vinculado=request.user)
        taf = Tarefa.objects.filter(vinculo=Us).order_by("-prioridade")
        serial = TarefaSerializer(taf, many=True)
        if len(serial.data) > 0:
            return Response({"status": 302, "Lista de Prioridade": serial.data})
        return Response({"status": 204, "msg": "No Content"})

    def create(self, request):
        titulo = request.data.get("titulo")
        desc = request.data.get("descricao")
        data = request.data.get("data_vencimento")
        p = request.data.get("prioridade")
        status = request.data.get("status")
        vinculo = Usuario.objects.get(Vinculado=request.user)
        Tarefa.objects.create(
            titulo=titulo,
            desc=desc,
            data_vencimento=data,
            prioridade=p,
            status=status,
            vinculo=vinculo,
        )
        return Response({"status": 201, "msg": "registered successfully"})

    def patch(self, request):
        id = request.data.get("id")
        taf = Tarefa.objects.get(id=id)
        titulo = request.data.get("titulo")
        desc = request.data.get("descricao")
        data = request.data.get("data_vencimento")
        p = request.data.get("prioridade")
        status = request.data.get("status")
        taf.titulo = titulo
        taf.desc = desc
        taf.data_vencimento = data
        taf.prioridade = p
        taf.status = status
        taf.save()
        return Response({"status": 200, "msg": "Updated!"})

    def delete(self, request):
        id = request.GET.get("id")
        taf = Tarefa.objects.get(id=id)
        taf.delete()
        return Response({"status": 200, "msg": "Deleted!"})
