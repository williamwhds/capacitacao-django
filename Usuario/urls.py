from rest_framework.routers import DefaultRouter

from .views import UsuarioModelViewSet

Urouter = DefaultRouter()
Urouter.register(r"Usuario", UsuarioModelViewSet, basename="Usuario")

urlpatterns = Urouter.urls
