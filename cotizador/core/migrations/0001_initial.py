# Generated by Django 2.2 on 2021-10-18 16:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=30, verbose_name='Nombre de empresa')),
                ('nombre_cliente', models.CharField(max_length=30, verbose_name='Nombre de Cliente')),
                ('mail_cliente', models.EmailField(max_length=30, verbose_name='Mail de Cliente')),
                ('informacion_nombre', models.CharField(max_length=30, verbose_name='Nombre primera pagina')),
                ('informacion_cuerpo', ckeditor.fields.RichTextField(default='De acuerdo a lo solicitado, adjunto presupuesto por el diseño de marca y etiqueta para micro cervecería. Quedando muy agradecido por la invitación a participar de este proyecto y seguros de dar respuesta a vuestras necesidades comunicacionales.', verbose_name='Texto primera pagina')),
                ('introduccion', ckeditor.fields.RichTextField(blank=True, default='BUENDÍA se encargará de diseñar y desarrollar la identidad coporativa para proyecto de tablas en madera. Buendía apuntará a crear una propuesta atractiva en términos visuales, con una imágen consistente, acordes al estado del arte, a necesidades operativas y comunicacionales del proyecto Taller Waye', null=True, verbose_name='Introduccion')),
                ('descuento', models.BooleanField(default=False, verbose_name='Descuento')),
                ('valor_descuento', models.PositiveIntegerField(blank=True, null=True, verbose_name='Cantidad descontada')),
                ('otros_comentarios', models.TextField(blank=True, null=True, verbose_name='Otros Comentarios')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Presupuesto',
                'verbose_name_plural': 'Presupuestos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del servicio')),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido del servicio')),
                ('tiempo', models.CharField(max_length=30, verbose_name='Tiempo estimado')),
                ('precio', models.PositiveIntegerField(verbose_name='Valor del servicio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ServicioPresupuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('presupuesto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Presupuesto')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Servicio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Servicio en Presupesto',
                'verbose_name_plural': 'Servicios en Presupuestos',
                'ordering': ['created'],
            },
        ),
    ]
