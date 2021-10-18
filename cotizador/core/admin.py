from django.contrib import admin
from .models import (
    Servicio,
    Presupuesto,
    ServicioPresupuesto
)

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

class PresupuestoAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Presupuesto, PresupuestoAdmin)
admin.site.register(ServicioPresupuesto)
