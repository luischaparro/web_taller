from django.contrib import admin
from django.urls import path
from taller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('datos/', views.datos, name="datos"),
    path('datos/crear', views.datos_crear, name="datos_crear"),
    path('datos/crear/documento', views.datos_crear_documento, name="datos_crear_documento"),
    path('datos/crear/ciudad', views.datos_crear_ciudad, name="datos_crear_ciudad"),
    path('datos/crear/persona', views.datos_crear_persona, name="datos_crear_persona"),
    path('datos/<int:dato_id>/D', views.datos_ver_D, name="datos_ver_D"),
    path('datos/<int:dato_id>/C', views.datos_ver_C, name="datos_ver_C"),
    path('datos/<int:dato_id>/P', views.datos_ver_P, name="datos_ver_P"),
]

