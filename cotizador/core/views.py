from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from django.views.generic import (
    CreateView, 
    UpdateView, 
    ListView
)

from .models import(
    Presupuesto,
    Servicio,
    ServicioPresupuesto
)

from .filters import(
    ServicioFilter,
    PresupuestoFilter
)

from .forms import(
    ServicioModelForm,
    PresupuestoModelForm,
    PresupuestoFormParteInicio,
    PresupuestoFormParteDos,
    PresupuestoFormParteTres,
    PresupuestoFormParteCuatro,
    ServicioPresupuestoModelForm,
    ServicioPresupuestoFormset,
    PresupuestoFormDescuento,
)

from pdflibs import sections, format
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, PageBreak
from django.http import FileResponse
import io

    #SERVICIOS

#INICIO PAGINA DE SERVICIOS TEMPLATE = servicios_inicio.html
class InicioServicio(ListView):
    model = Servicio
    ordering = ['-created']
    template_name = 'core/servicios_inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ServicioFilter(self.request.GET, queryset=self.get_queryset())
        return context

#CREAR NUEVO SERVICIO = servicios_crear.html
class CrearServicio(LoginRequiredMixin, CreateView):
    model = Servicio
    form_class = ServicioModelForm
    template_name = 'core/servicios_crear.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "El servicio fue creado con exito")
        return super().form_valid(form)


#MODIFICACION DE SERVICIOS ESPESIFICO TEMPLATE = servicios_edicio.html
class EdicionServicio(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Servicio
    form_class = ServicioModelForm
    template_name = 'core/servicios_edicion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "El servicio fue editado con exito")
        return super().form_valid(form)

    def test_func(self):
        formulario = self.get_object()
        if self.request.user == formulario.usuario:
            return True
        return False

#ELIMINACION DE SERVICIOS = servicios_delete.html
@login_required
def servicio_delete(request, pk):
    servicio = Servicio.objects.get(pk=pk)

    if request.method == 'POST':
        if request.user == servicio.usuario:
            servicio.delete()
            messages.success(request, f'El servicio fue elimiado con exito')
            return redirect('servicios-inicio')
        else:
            messages.warning(request, f'No esta autorizado para eliminar el servicio')
            return redirect('servicios-inicio')
    context = {
        'object': servicio,
    }

    return render(request, 'core/servicios_delete.html', context)

    #PRESUPUESTO
# = servicios_edicio.html

class EdicionServicioPresupuesto(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = ServicioPresupuesto
    form_class = ServicioPresupuestoModelForm
    template_name = 'core/serviciopresupuesto_edicion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "El servicio fue editado con exito")
        return super().form_valid(form)

    def test_func(self):
        formulario = self.get_object()
        if self.request.user == formulario.usuario:
            return True
        return False

@login_required
def serviciopresupuesto_delete(request, pk):
    serviciopresupuesto = ServicioPresupuesto.objects.get(pk=pk)
    presupuesto = serviciopresupuesto.presupuesto
    presupuesto_id = presupuesto.id

    if request.method == 'POST':
        serviciopresupuesto.delete()
        messages.success(request, f'El presupuesto fue elimiado con exito')
        return redirect('presupuesto-crear-4', presupuesto_id)

    context = {
        'object': serviciopresupuesto,
    }

    return render(request, 'core/serviciopresupuesto_delete.html', context)


    #PRESUPUESTO
#MODIFICACION DE SERVICIOS ESPESIFICO TEMPLATE = servicios_edicio.html
class InicioPresupuesto(ListView):
    model = Presupuesto
    ordering = ['-created']
    template_name = 'core/presupuesto_inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PresupuestoFilter(self.request.GET, queryset=self.get_queryset())
        return context

#MODIFICACION DE SERVICIOS ESPESIFICO TEMPLATE = servicios_edicio.html
class EdicionPresupuesto(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Presupuesto
    form_class = PresupuestoModelForm
    template_name = 'core/presupuesto_edicion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        messages.success(self.request, "El servicio fue editado con exito")
        return super().form_valid(form)

    def test_func(self):
        formulario = self.get_object()
        if self.request.user == formulario.usuario:
            return True
        return False

#MODIFICACION DE SERVICIOS ESPESIFICO TEMPLATE = servicios_edicio.html
@login_required
def presupuesto_delete(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)

    if request.method == 'POST':
        if request.user == presupuesto.usuario:
            presupuesto.delete()
            messages.success(request, f'El presupuesto fue elimiado con exito')
            return redirect('presupuesto-inicio')
        else:
            messages.warning(request, f'No esta autorizado para eliminar el presupuesto')
            return redirect('presupuesto-inicio')
    context = {
        'object': presupuesto,
    }

    return render(request, 'core/presupuesto_delete.html', context)

@login_required
def presupuesto_duplicar(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    servicios = ServicioPresupuesto.objects.filter(presupuesto=pk)

    if request.method == 'POST':
        n_presupuesto = Presupuesto.objects.create(
            nombre_empresa=presupuesto.nombre_empresa,
            nombre_cliente=presupuesto.nombre_cliente,
            mail_cliente=presupuesto.mail_cliente,
            informacion_nombre=presupuesto.informacion_nombre,
            informacion_cuerpo=presupuesto.informacion_cuerpo,
            introduccion=presupuesto.introduccion,
            descuento=presupuesto.descuento,
            valor_descuento=presupuesto.valor_descuento,
            otros_comentarios=presupuesto.otros_comentarios,
            usuario=request.user,
        )
        for servicio in servicios:
            n_servicio = ServicioPresupuesto.objects.create(
                servicio=servicio.servicio,
                presupuesto=n_presupuesto,
                descripcion=servicio.descripcion,
                usuario=request.user,
            )
        messages.success(request, f'El fue duplicado')
        return redirect('presupuesto-inicio')

    context = {
        'presupuesto': presupuesto,
        'servicios':servicios,
    }

    return render(request, 'core/presupuesto_duplicar.html', context)


#MODIFICACION DE SERVICIOS ESPESIFICO TEMPLATE = servicios_edicio.html
@login_required
def presupuesto_crear_inicio(request):
    form = PresupuestoFormParteInicio()
    
    if request.method == 'POST':
        form = PresupuestoFormParteInicio(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            presupuesto = obj.id
            return redirect('presupuesto-crear-2',pk=presupuesto)
        
    else:
        form = PresupuestoFormParteInicio()
    
    context = {
        'form': form,
    }

    return render(request, 'core/presupuesto_crear_1.html', context)

@login_required
def presupuesto_crear_dos(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    formset = ServicioPresupuestoFormset()
    form = PresupuestoFormParteDos()
    
    if request.method == 'POST':
        form = PresupuestoFormParteDos(request.POST)
        formset = ServicioPresupuestoFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            presupuesto.introduccion = form.cleaned_data.get('introduccion')
            presupuesto.save()
            presupuesto_id = presupuesto.id
            for form in formset:
                servicio = form.cleaned_data.get('servicio')
                descripcion = servicio.descripcion
                if servicio:
                    ServicioPresupuesto(
                        servicio=servicio,
                        presupuesto=presupuesto,
                        descripcion=descripcion,
                        usuario=request.user
                        ).save()
            return redirect('presupuesto-crear-3', pk=presupuesto_id)
        
    else:
        form = PresupuestoFormParteDos()
    
    context = {
        'form': form,
        'formset':formset,
    }

    return render(request, 'core/presupuesto_crear_2.html', context)

@login_required
def presupuesto_crear_tres(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    servicios = ServicioPresupuesto.objects.filter(presupuesto=pk) 
    
    
    context = {
        'servicios':servicios,
        'presupuesto':presupuesto,
    }

    return render(request, 'core/presupuesto_crear_3.html', context)


@login_required
def presupuesto_crear_cuatro(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    servicios = ServicioPresupuesto.objects.filter(presupuesto=pk)
    form = PresupuestoFormParteCuatro()
    descuento = PresupuestoFormDescuento()

    s_list = [servicio for servicio in servicios.values()]
    total = calcular_total(servicios, s_list, 0)

    if request.method == 'POST':
        form = PresupuestoFormParteCuatro(request.POST)
        descuento = PresupuestoFormDescuento(request.POST)
        if form.is_valid() and descuento.is_valid():
            presupuesto.descuento = descuento.cleaned_data.get('descuento')
            presupuesto.valor_descuento = descuento.cleaned_data.get('valor_descuento')
            presupuesto.otros_comentarios = form.cleaned_data.get('otros_comentarios')
            presupuesto.save()
            presupuesto = presupuesto.id
            return redirect('presupuesto-crear-5', presupuesto)
        
    else:
        form = PresupuestoFormParteCuatro()
    
    context = {
        'form': form,
        'servicios':servicios,
        'descuento':descuento,
        'total':total
    }

    return render(request, 'core/presupuesto_crear_4.html', context)

@login_required
def presupuesto_crear_cinco(request, pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    servicios = ServicioPresupuesto.objects.filter(presupuesto=pk)
    s_list = [servicio for servicio in servicios.values()]
    if presupuesto.descuento == True:
        total = calcular_total(servicios, s_list, presupuesto.valor_descuento)
    else:
        total = calcular_total(servicios, s_list, 0)
    
    context = {
        'presupuesto': presupuesto,
        'servicios':servicios,
        'total':total,
    }

    return render(request, 'core/presupuesto_crear_5.html', context)


def calcular_total(queryset, servicios, valor_descuento):
    total = 0
    for servicio in servicios:
        ser = Servicio.objects.get(pk=servicio['servicio_id'])
        precio = ser.precio
        total = total + precio
    total = total - valor_descuento
    return total


@login_required
def presupuesto_pdf(request,pk):
    presupuesto = Presupuesto.objects.get(pk=pk)
    servicios = ServicioPresupuesto.objects.filter(presupuesto=pk)
    lista_presupuesto = []
    lista_servicios = {}

    datos_presupuesto={
        'id_presupuesto': presupuesto.id,
        'nombre_cliente': presupuesto.nombre_cliente,
        'nombre_empresa': presupuesto.nombre_empresa,
        'tipo_proyecto': 'Portal Web'}
    
    datos_portada = {
        'titulo_saludo': presupuesto.informacion_nombre,
        'texto_saludo': presupuesto.informacion_cuerpo,
        'firma_saludo': "<b>Equipo Buen día</b>"}
    
    lista_presupuesto.append(datos_presupuesto)
    lista_presupuesto.append(datos_portada)

    for servicio in servicios:
        serv = {
            f"{servicio.servicio.nombre}": {
                'precio':servicio.servicio.precio,
                'descripcion':servicio.descripcion,
                'tiempo':servicio.servicio.tiempo,
            }
        }
        lista_servicios.update(serv)

    #print(lista_presupuesto)
    #print(lista_servicios)
    
    buf = io.BytesIO()
    #generarPDF(lista_presupuesto, lista_servicios)
    buffer, nombre = generarPDF(lista_presupuesto, lista_servicios)

    return FileResponse(buffer, as_attachment=True, filename=nombre)

    #context = {
        #'presupuesto':presupuesto,
    #}

    #return render(request, 'core/presupuesto_pdf.html', context)



def generarPDF(lista_presupuesto, datos_servicios):

    hoja = 'carta'
    fuente = 'Poppins'
    folio = lista_presupuesto[0]['id_presupuesto']
    numero_pagina = 2
    numero_servicio = 1

    datos_presupuesto = lista_presupuesto[0]
    datos_portada = lista_presupuesto[1]
    datos_contacto =  {
        'nombre_empresa': '<b>Agencia de Diseño Buendía</b>',
        'direccion': 'Eliodoro Yáñez 1110 Of. E. Providencia - Santiago, Chile',
        'telefono': 'Fono of. <b>+56 2 2235 4334</b>',
        'correo': 'info@buendia.cl',
        'sitio': '<a href="http://www.buendia.cl"><b>www.buendia.cl</b></a>'}

    buf = io.BytesIO()
    ppto = canvas.Canvas(buf)
    documento, estilos = format.setDocumentProperties(hoja, fuente, folio)
    #datos_contacto, datos_presupuesto, datos_portada, datos_servicios  = data.getData()

    sections.portada(ppto, documento, estilos, datos_contacto, datos_portada)
    numero_servicio, numero_pagina = sections.servicios(ppto, documento, estilos, datos_presupuesto, datos_contacto, datos_servicios, numero_pagina, numero_servicio)
    numero_pagina = sections.metodologia(ppto, documento, estilos, datos_presupuesto, datos_contacto, numero_pagina, numero_servicio)
    sections.propuesta(ppto, documento, estilos, datos_presupuesto, datos_contacto, datos_servicios, numero_pagina, numero_servicio)
    
    ppto.save()
    buf.seek(0)

    return buf, f"Presupuesto-{folio}.pdf"
