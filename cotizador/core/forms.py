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
        fields = ['descripcion','precio','tiempo']

class ServicioPresupuestoForm(forms.ModelForm):
    class Meta:
        model = ServicioPresupuesto
        fields = ['servicio']
ServicioPresupuestoFormset = inlineformset_factory(Presupuesto,
                                                ServicioPresupuesto,
                                                form=ServicioPresupuestoForm,
                                                can_delete=False,
                                                extra=1)


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
            'iva',
            'valor_descuento',
        ]
        widgets = {
        }                    
    

