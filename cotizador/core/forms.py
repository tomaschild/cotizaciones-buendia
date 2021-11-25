from django import forms
from django.forms import inlineformset_factory
from .models import (
    Presupuesto,
    Servicio,
    ServicioPresupuesto
)


class ServicioModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServicioModelForm,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Servicio
        fields = [
            'nombre',
            'descripcion',
            'tiempo',
            'precio',
        ]
        widgets = {
        }

class ServicioPresupuestoModelForm(forms.ModelForm):
    class Meta:
        model = ServicioPresupuesto
        fields = ['descripcion']

class ServicioPresupuestoForm(forms.ModelForm):
    class Meta:
        model = ServicioPresupuesto
        fields = ['servicio']
ServicioPresupuestoFormset = inlineformset_factory(Presupuesto,
                                                ServicioPresupuesto,
                                                form=ServicioPresupuestoForm,
                                                can_delete=False,
                                                extra=1)

# nombre_empresa = models.CharField(max_length=30, verbose_name='Nombre de empresa')
# nombre_cliente = models.CharField(max_length=30, verbose_name='Nombre de Cliente')
# mail_cliente = models.EmailField(max_length=30, verbose_name='Mail de Cliente')
# servicios_presupuesto = models.CharField(max_length=30, verbose_name='Servicios del Presupuesto')
# informacion_nombre = models.CharField(max_length=30, verbose_name='Nombre primera pagina')
# informacion_cuerpo = models.TextField(
#     default='De acuerdo a lo solicitado, adjunto presupuesto por el diseño de marca y etiqueta para micro cervecería. Quedando muy agradecido por la invitación a participar de este proyecto y seguros de dar respuesta a vuestras necesidades comunicacionales.',
#     verbose_name='Texto primera pagina'
# )
# introduccion = models.TextField(
#     default='BUENDÍA se encargará de diseñar y desarrollar la identidad coporativa para proyecto de tablas en madera. Buendía apuntará a crear una propuesta atractiva en términos visuales, con una imágen consistente, acordes al estado del arte, a necesidades operativas y comunicacionales del proyecto Taller Waye',
#     verbose_name='Introduccion',
#     blank=True,
#     null=True
# )
# descuento = models.BooleanField(default=False, verbose_name="Descuento")
# valor_descuento = models.PositiveIntegerField(verbose_name='Cantidad descontada',null=True, blank=True)
# otros_comentarios = models.TextField(verbose_name='Otros Comentarios', null=True, blank=True)

# usuario = models.ForeignKey(User, on_delete=models.PROTECT)
# created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", editable=False)
# updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", editable=False)

class PresupuestoModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresupuestoModelForm,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Presupuesto
        fields = [
            'nombre_empresa',
            'nombre_cliente',
            'tipo',
            'mail_cliente',
            'informacion_nombre',
            'informacion_cuerpo',
            'introduccion',
            'descuento',
            'valor_descuento',
            'otros_comentarios',
        ]
        widgets = {
        }

class PresupuestoFormParteInicio(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresupuestoFormParteInicio,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Presupuesto
        fields = [
            'nombre_empresa',
            'nombre_cliente',
            'mail_cliente',
            'tipo',
            'informacion_nombre',
            'informacion_cuerpo',
        ]
        widgets = {
        }

class PresupuestoFormParteDos(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresupuestoFormParteDos,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Presupuesto
        fields = [
            'introduccion',
        ]
        widgets = {
        }

class PresupuestoFormParteTres(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresupuestoFormParteTres,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Presupuesto
        fields = [
            'introduccion',
        ]
        widgets = {
        }

class PresupuestoFormParteCuatro(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresupuestoFormParteCuatro,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Presupuesto
        fields = [
            'otros_comentarios',
        ]
        widgets = {
        }

class PresupuestoFormDescuento(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresupuestoFormDescuento,self).__init__(*args, **kwargs)
    
    class Meta:
        model = Presupuesto
        fields = [
            'descuento',
            'valor_descuento',
        ]
        widgets = {
        }                    
            