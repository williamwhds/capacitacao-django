from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from .serializer import UsuarioSerializer


class UsuarioModelViewSet(ModelViewSet):
    # authenticacao
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def list(self, request):
        usuarios = Usuario.objects.all()
        serial = UsuarioSerializer(usuarios, many=True)
        if len(serial.data) > 0:
            return Response({"status": 302, "Usuarios": serial.data})
        return Response({"status": 204, "msg": "No cotent"})

    def create(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        hashed_password = make_password(password)
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            response_data = {
                "status": 409,
                "errorType": "NameError",
                "errorAt": "username",
            }
            return JsonResponse(response_data, status=409)
        else:
            name = request.data.get("first name")
            email = request.data.get("email")
            tel = request.data.get("telefone")
            cpf = request.data.get("cpf")
            usuario = User.objects.create(
                username=username,
                password=hashed_password,
                first_name=name,
                email=email,
            )
            user = Usuario.objects.create(vinculado=usuario, telefone=tel, cpf=cpf)
            user.save()
            usuario.save()

            return Response({"status": 200, "msg": "Created!"})

    def patch(self, request):
        obj = Usuario.objects.get(Vinculado=request.user)
        name = request.data.get("first name")
        email = request.data.get("email")
        tel = request.data.get("telefone")
        cpf = request.data.get("cpf")
        obj.Vinculado.first_name = name
        obj.Vinculado.email = email
        obj.Telefone = tel
        obj.cpf = cpf
        obj.Vinculado.save()
        obj.save()
        return Response({"status": 200, "msg": "OK"})

    def delete(self, request):
        id = request.GET.get("id")
        obj = Usuario.objects.get(id=id)
        obj.Vinculado.delete()
        obj.delete()
        return Response({"status": 200, "msg": "Deleted"})
