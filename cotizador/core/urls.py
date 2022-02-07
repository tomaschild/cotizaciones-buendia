from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import (
  #SERVICIOS
  InicioServicio,
  EdicionServicio,
  CrearServicio,
  #SERVICIO PRESUPUESTO
  # EdicionServicioPresupuesto,
  #PRESUPUESTO
  InicioPresupuesto,
)

urlpatterns = [
  path('',TemplateView.as_view(template_name='core/home.html'),name="core-home"),
  #PRESUPUESTOS
  path('presupuesto/',InicioPresupuesto.as_view(),name="presupuesto-inicio"),
  path('presupuesto/edicion/<int:pk>',views.edicion_presupuesto,name="presupuesto-edicion"),
  path('presupuesto/crear/',views.presupuesto_crear_inicio,name="presupuesto-crear-1"),
  path('presupuesto/crear/<int:pk>/',views.presupuesto_crear_dos,name="presupuesto-crear-2"),
  path('presupuesto/crear/resumen/<int:pk>/',views.presupuesto_crear_tres,name="presupuesto-crear-3"),
  path('presupuesto/crear/precio/<int:pk>/',views.presupuesto_crear_cuatro,name="presupuesto-crear-4"),
  path('presupuesto/crear/precio/final/<int:pk>/',views.presupuesto_crear_cinco,name="presupuesto-crear-5"),
  path('presupuesto/<int:pk>/delete/',views.presupuesto_delete, name='presupuesto-delete'),
  path('presupuesto/<int:pk>/duplicar/',views.presupuesto_duplicar, name='presupuesto-duplicar'),
  path('presupuesto/<int:pk>/pdf/',views.presupuesto_pdf, name='presupuesto-pdf'),
  #SEWRVICIOS Presupuesto
  path('serviciopresupuesto/<int:pk>/edicion/<int:redireccion>/',views.edicion_servicio_presupuesto, name="serviciopresupuesto-edicion"),
  path('serviciopresupuesto/<int:pk>/delete/<int:redireccion>/',views.serviciopresupuesto_delete, name="serviciopresupuesto-delete"),
  #SEWRVICIOS
  path('servicios/',InicioServicio.as_view(),name="servicios-inicio"),
  path('servicios/crear/',CrearServicio.as_view(),name="servicios-crear"),
  path('servicios/<int:pk>/edicion/',EdicionServicio.as_view(),name="servicios-edicion"),
  path('servicios/<int:pk>/delete/',views.servicio_delete, name='servicios-delete'),
]