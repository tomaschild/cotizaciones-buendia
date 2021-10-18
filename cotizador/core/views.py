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
    ServicioPresupuestoFormset
)


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
    
    if request.method == 'POST':
        form = PresupuestoFormParteCuatro(request.POST)
        if form.is_valid():
            presupuesto.descuento = form.cleaned_data.get('descuento')
            presupuesto.valor_descuento = form.cleaned_data.get('valor_descuento')
            presupuesto.otros_comentarios = form.cleaned_data.get('otros_comentarios')
            presupuesto.save()
            presupuesto = presupuesto.id
            return redirect('presupuesto-inicio')
        
    else:
        form = PresupuestoFormParteCuatro()
    
    context = {
        'form': form,
        'servicios':servicios,
    }

    return render(request, 'core/presupuesto_crear_4.html', context)