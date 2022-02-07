from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

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
    iva = models.BooleanField(default=True, verbose_name="IVA")
    valor_descuento = models.DecimalField(max_digits=3,decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR,verbose_name='Porcentaje de descuento',null=True, blank=True)
    otros_comentarios = RichTextField(verbose_name='Otros Comentarios', null=True, blank=True, default= f" \
    <p>&bull; Los valores expresados son totales. Contemplan factura excenta de IVA por servicios profesionales de dise&ntilde;o.</p>\
    \
    <p>&bull; Los valores aqu&iacute; expresados no incluyen costos de servidor ni dominio. Buend&iacute;a puede gestioar su adquisici&oacute;n.</p>\
    \
    <p>&bull; Los plazos est&aacute;n sujetos a entrega de Orden de Compra, contenidos y feedback por parte de cliente.</p>\
    \
    <p>&bull; Todos los servicios tienen una garant&iacute;a por 3 meses a partir de la fecha de entrega.</p>\
    \
    <p>&bull; Forma de pago sugerida. 50% anticipo y 50% contra entrega final del proyecto.</p>\
    \
    <p>&nbsp;</p>\
    \
    <p>Datos de la Empresa</p>\
    \
    <p>Castro y Vicencio C&iacute;a. Ltda.</p>\
    \
    <p>76.084.268-0</p>\
    \
    <p>Servicios de dise&ntilde;o gr&aacute;fico</p>\
    \
    <p>Garibaldi 1653, &Ntilde;u&ntilde;oa - Santiago.</p>")

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
    tiempo = models.CharField(default="20 dias habiles",max_length=30, verbose_name='Tiempo estimado')
    precio = models.PositiveIntegerField(default=0,verbose_name='Valor del servicio')

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