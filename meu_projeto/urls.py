from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from Tarefa.urls import Trouter

from Usuario.urls import Urouter

urlpatterns = [
    path("admin", admin.site.urls),
    path("login", views.obtain_auth_token),
    path("", include(Urouter.urls)),
    path("", include(Trouter.urls)),
]
