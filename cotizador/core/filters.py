import django_filters
from .models import (
    Presupuesto,
    Servicio,
)

class ServicioFilter(django_filters.FilterSet):
    nombre_filtro = django_filters.CharFilter(label='Nombre del Servicio',field_name='nombre',lookup_expr='icontains')
    
    class Meta:
        model = Servicio
        fields = {
        }

class PresupuestoFilter(django_filters.FilterSet):
    nombre_empresa_filtro = django_filters.CharFilter(label='Nombre de la empresa',field_name='nombre_empresa',lookup_expr='icontains')
    
    class Meta:
        model = Presupuesto
        fields = {
        }
    