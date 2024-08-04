"""
URL configuration for AppFotos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.db import router
from django.urls import include, path
from galeria import views as galeria_views  # Importa las vistas de tu aplicación 'galeria'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', galeria_views.lista_tareas, name='lista_tareas'),
    path('tareas/<int:tarea_id>/', galeria_views.detalle_tarea, name='detalle_tarea'),
    path('crear-tarea/', galeria_views.crear_tarea, name='crear_tarea'),  # URL para crear nueva tarea
    path('descargar_fotos/<int:nota_id>/', galeria_views.descargar_fotos_nota, name='descargar_fotos_nota'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

