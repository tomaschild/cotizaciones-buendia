from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from ckeditor.fields import RichTextField

class Presupuesto(models.Model):
    nombre_empresa = models.CharField(max_length=30, verbose_name='Nombre de empresa')
    nombre_cliente = models.CharField(max_length=30, verbose_name='Nombre de Cliente')
    tipo = models.CharField(max_length=30, verbose_name='Tipo de Proyecto')
    mail_cliente = models.EmailField(max_length=30, verbose_name='Mail de Cliente')
    informacion_nombre = models.CharField(max_length=30, verbose_name='Nombre primera pagina')
    informacion_cuerpo = RichTextField(
        default='De acuerdo a lo solicitado, adjunto presupuesto por el diseño de marca y etiqueta para micro cervecería. Quedando muy agradecido por la invitación a participar de este proyecto y seguros de dar respuesta a vuestras necesidades comunicacionales.',
        verbose_name='Texto primera pagina'
    )
    introduccion = RichTextField(
        default='BUENDÍA se encargará de diseñar y desarrollar la identidad coporativa para proyecto de tablas en madera. Buendía apuntará a crear una propuesta atractiva en términos visuales, con una imágen consistente, acordes al estado del arte, a necesidades operativas y comunicacionales del proyecto Taller Waye',
        verbose_name='Introduccion',
        blank=True,
        null=True
    )
    descuento = models.BooleanField(default=False, verbose_name="Descuento")
    valor_descuento = models.PositiveIntegerField(verbose_name='Cantidad descontada',null=True, blank=True)
    otros_comentarios = RichTextField(verbose_name='Otros Comentarios', null=True, blank=True)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", editable=False)

    class Meta:
        verbose_name = "Presupuesto"
        verbose_name_plural = "Presupuestos"
        ordering = ['-created']

    def __str__(self):
        return f'{self.nombre_empresa} - {self.nombre_cliente}'

    def  get_absolute_url(self):
        return reverse('presupuesto-inicio') 

class Servicio(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre del servicio')
    descripcion = RichTextField(null=True, blank=True,verbose_name='Contenido del servicio')
    tiempo = models.CharField(max_length=30, verbose_name='Tiempo estimado')
    precio = models.PositiveIntegerField(verbose_name='Valor del servicio')

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", editable=False)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}'

    def  get_absolute_url(self):
        return reverse('servicios-inicio') 

class ServicioPresupuesto(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    presupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    descripcion = RichTextField(null=True,blank=True)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", editable=False)

    class Meta:
        verbose_name = "Servicio en Presupesto"
        verbose_name_plural = "Servicios en Presupuestos"
        ordering = ['-created']

    def __str__(self):
        return f'{self.presupuesto.id} - {self.servicio}'
    
    def  get_absolute_url(self):
        return reverse('presupuesto-crear-3', kwargs={'pk': self.presupuesto.id})