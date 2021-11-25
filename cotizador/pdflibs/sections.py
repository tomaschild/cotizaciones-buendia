import os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, PageBreak
from reportlab.lib.styles import ParagraphStyle


RUTA_IMAGEN_PORTADA = "/pdflibs/images/cover-top.png"
RUTA_LOGO = "/pdflibs/images/logo.png"
RUTA_DISENO = "/pdflibs/images/logo-diseno.jpg"
RUTA_METODOLOGIA = "/pdflibs/images/metodologia.png"
base = os.getcwd()


def portada(presupuesto, documento, estilos, datos_contacto, datos_portada):
    
    #Imagen de cabecera de la portada
    presupuesto.drawImage(base+RUTA_IMAGEN_PORTADA, 0, documento['alto_documento']-100, width=documento['ancho_documento'], height=150)
    
    x = documento['ancho_documento']/2
    y = (documento['alto_documento']/2)+150
    
    #Título de la portada
    parrafo = Paragraph(datos_portada['titulo_saludo'], estilos['titulo_presentacion'])
    width, height = parrafo.wrap(200, 500)
    parrafo.drawOn(presupuesto, (x - width/2), y)
    y -= height
    
    #Cuerpo de la portada
    parrafo = Paragraph(datos_portada['texto_saludo'], estilos['body_presentacion'])
    width, height = parrafo.wrap(200, 500)
    y -= height
    parrafo.drawOn(presupuesto, (x - width/2), y)
    
    #Firma
    parrafo = Paragraph(datos_portada['firma_saludo'], estilos['firma_presentacion'])
    width, height = parrafo.wrap(200, 500)
    y -= height
    parrafo.drawOn(presupuesto, (x - width/2), y)
    y = 150

    #Pie de página
    parrafo = Paragraph(datos_contacto['nombre_empresa'], estilos['contacto_presentacion'])
    width, height = parrafo.wrap(200, 100)
    parrafo.drawOn(presupuesto, (x - width/2), y)
    y -= 20

    parrafo = Paragraph(datos_contacto['direccion'], estilos['contacto_presentacion'])
    width, height = parrafo.wrap(200, 100)
    y -= height
    parrafo.drawOn(presupuesto, (x - width/2), y)

    parrafo = Paragraph(datos_contacto['telefono'], estilos['contacto_presentacion'])
    width, height = parrafo.wrap(200, 100)
    y -= height
    parrafo.drawOn(presupuesto, (x - width/2), y)

    parrafo = Paragraph(datos_contacto['correo'], estilos['contacto_presentacion'])
    width, height = parrafo.wrap(200, 100)
    y -= height
    parrafo.drawOn(presupuesto, (x - width/2), y)

    parrafo = Paragraph(datos_contacto['sitio'], estilos['contacto_presentacion'])
    width, height = parrafo.wrap(200, 100)
    y -= height
    parrafo.drawOn(presupuesto, (x - width/2), y)

    #Nueva página
    presupuesto.showPage()


def servicios(presupuesto, documento, estilos, datos_presupuesto, datos_contacto, datos_servicios, numero_pagina, numero_servicio):

    numero_servicio = 1
    espacio = documento['alto_documento'] - 250
    x = 30
    y = espacio + 150
    
    cabecera(presupuesto, documento, estilos, datos_presupuesto)
    pieDePagina(presupuesto, documento, estilos, datos_contacto, numero_pagina)
    
    for servicio in datos_servicios:

        titulo, descripcion, dimensiones = calcularTamanoServicio(servicio, datos_servicios, estilos, numero_servicio, documento)
        numero_servicio += 1
            
        if espacio - dimensiones['alto_total'] > 300:
            y -= dimensiones['alto_titulo']+20
            titulo.drawOn(presupuesto, x, y)
            y -= dimensiones['alto_descripcion']+30
            descripcion.drawOn(presupuesto, x, y)
            espacio -= dimensiones['alto_total']

        else:
            presupuesto.showPage()
            cabecera(presupuesto, documento, estilos, datos_presupuesto)
            pieDePagina(presupuesto, documento, estilos, datos_contacto, numero_pagina)
            numero_pagina += 1
            espacio = documento['alto_documento'] - 250
            y = espacio + 150

    return numero_servicio, numero_pagina


def metodologia(presupuesto, documento, estilos, datos_presupuesto, datos_contacto, numero_pagina, numero_servicio):
    
    presupuesto.showPage()
    numero_pagina += 1
    titulo = Paragraph(f"{numero_servicio}. METODOLOGÍA", estilos['titulo_servicio'])
    titulo.wrap(documento['ancho_documento']-60, documento['alto_documento']-300)
    titulo.drawOn(presupuesto, 30, documento['alto_documento']-150)
    
    descripcion = Paragraph('<b>En buendía utilizamos una metodología basada en el concepto Design Thinking</b>, la cual hemos simplificado en función de cada tipo de proyecto y necesidad de diseño.', estilos['body_servicios'])
    descripcion.wrap(documento['ancho_documento']-60, documento['alto_documento']-300)
    descripcion.drawOn(presupuesto, 30, documento['alto_documento']-200)
    
    cabecera(presupuesto, documento, estilos, datos_presupuesto)
    pieDePagina(presupuesto, documento, estilos, datos_contacto, numero_pagina)
    presupuesto.drawImage(base+RUTA_METODOLOGIA,
                          0, documento['alto_documento']-600,
                          width=documento['ancho_documento'],
                          height=documento['alto_documento']-450)
    
    return numero_pagina
    

def cabecera(presupuesto, documento, estilos, datos_presupuesto):
    
    x = documento['ancho_documento']/2
    
    #Logo
    presupuesto.drawImage(base+RUTA_LOGO, 30, documento['alto_documento']-30, 140, 80)
    
    #Folio y fecha
    parrafo = Paragraph(documento['folio'], estilos['header_fecha'])
    width, height = parrafo.wrap(150, 50)
    y = documento['alto_documento'] - height
    parrafo.drawOn(presupuesto, documento['ancho_documento'] - width, y)
    
    #Datos del cliente
    presupuesto.setStrokeColorRGB(0,0,0,0)
    presupuesto.setFillColor(HexColor('#EEEEEE'))
    y = documento['alto_documento'] - 100
    presupuesto.rect(0, y, documento['ancho_documento'], 40, stroke=1, fill=1)

    parrafo = Paragraph('Cliente', estilos['header_datos_cliente'])
    width, height = parrafo.wrap(100, 100)
    y = documento['alto_documento'] - 80
    x = 150
    parrafo.drawOn(presupuesto, x, y)
    
    parrafo = Paragraph('Encargado por', estilos['header_datos_cliente'])
    width, height = parrafo.wrap(100, 100)
    x += (documento['ancho_documento']-150)/3
    parrafo.drawOn(presupuesto, x, y)

    parrafo = Paragraph('Tipo proyecto', estilos['header_datos_cliente'])
    width, height = parrafo.wrap(100, 100)
    x += (documento['ancho_documento']-150)/3
    parrafo.drawOn(presupuesto, x, y)
    
    parrafo = Paragraph(datos_presupuesto['nombre_empresa'], estilos['datos_cliente'])
    width, height = parrafo.wrap(150, 100)
    y -= height
    x = 150
    parrafo.drawOn(presupuesto, x, y)

    parrafo = Paragraph(datos_presupuesto['nombre_cliente'], estilos['datos_cliente'])
    width, height = parrafo.wrap(150, 100)
    x += (documento['ancho_documento']-150)/3
    parrafo.drawOn(presupuesto, x, y)

    parrafo = Paragraph(datos_presupuesto['tipo_proyecto'], estilos['datos_cliente'])
    width, height = parrafo.wrap(150, 100)
    x += (documento['ancho_documento']-150)/3
    parrafo.drawOn(presupuesto, x, y)
    

def pieDePagina(presupuesto, documento, estilos, datos_contacto, numero_pagina):
    
    x = 100

    presupuesto.setStrokeColorRGB(0,0,0,0)
    presupuesto.setFillColor(HexColor('#EEEEEE'))
    presupuesto.rect(0, 100, documento['ancho_documento'], 5, stroke=1, fill=1)

    parrafo = Paragraph('Estudio de Diseño Buendia.', estilos['header_fecha'])
    width, height = parrafo.wrap(500, 100)
    parrafo.drawOn(presupuesto, x, 70)

    parrafo = Paragraph(datos_contacto['direccion'], estilos['contacto_servicios'])
    width, height = parrafo.wrap(200, 100)
    parrafo.drawOn(presupuesto, x, 40)

    parrafo = Paragraph(datos_contacto['telefono']+' / '+datos_contacto['correo'], estilos['contacto_servicios'])
    width, height = parrafo.wrap(200, 100)
    parrafo.drawOn(presupuesto, x, 30)

    parrafo = Paragraph(datos_contacto['sitio'], estilos['contacto_servicios'])
    width, height = parrafo.wrap(200, 100)
    parrafo.drawOn(presupuesto, x, 20)

    #numero de pagina
    parrafo = Paragraph(str(numero_pagina), estilos['firma_presentacion'])
    width, height = parrafo.wrap(200, 100)
    parrafo.drawOn(presupuesto, 50, 45)

    parrafo = Paragraph('Somos asociados <br/>a Chile Diseño', estilos['body_servicios'])
    width, height = parrafo.wrap(200, 100)
    parrafo.drawOn(presupuesto, documento['ancho_documento']-200, 45)

    presupuesto.drawImage(base+RUTA_DISENO, documento['ancho_documento']-100, 30, width=40, height=50)


def calcularTamanoServicio(servicio, datos_servicios, estilos, numero_servicio, documento):
 
    dimensiones = {
        'ancho_titulo': 0,
        'alto_titulo': 0,
        'ancho_descripcion': 0,
        'alto_descripcion': 0,
        'alto_total': 0
    }
    
    titulo = Paragraph(f"{numero_servicio}. {servicio}", estilos['titulo_servicio'])
    dimensiones['ancho_titulo'], dimensiones['alto_titulo'] = titulo.wrap(documento['ancho_documento']-60, documento['alto_documento']-300)

    descripcion = Paragraph(datos_servicios[servicio]['descripcion'], estilos['body_servicios'])
    dimensiones['ancho_descripcion'], dimensiones['alto_descripcion'] = descripcion.wrap(documento['ancho_documento']-60, documento['alto_documento']-300)
    
    dimensiones['alto_total'] = dimensiones['alto_descripcion']+dimensiones['alto_titulo']

    return titulo, descripcion, dimensiones


def propuesta(presupuesto, documento, estilos, datos_presupuesto, datos_contacto, datos_servicios, numero_pagina, numero_servicio):
    
    presupuesto.showPage()
    numero_pagina += 1
    titulo = Paragraph(f"{numero_servicio}. PROPUESTA ECONÓMICA", estilos['titulo_servicio'])
    titulo.wrap(documento['ancho_documento']-60, documento['alto_documento']-300)
    titulo.drawOn(presupuesto, 30, documento['alto_documento']-150)
    
    descripcion = Paragraph('<b>La propuesta económica</b> presentada a continuación contempla la totalidad de la solución según lo descrito anteriormente, incluyendo la toma de requerimientos e implementación.', estilos['body_servicios'])
    descripcion.wrap(documento['ancho_documento']-60, documento['alto_documento']-300)
    descripcion.drawOn(presupuesto, 30, documento['alto_documento']-200)
    
    cabecera(presupuesto, documento, estilos, datos_presupuesto)
    pieDePagina(presupuesto, documento, estilos, datos_contacto, numero_pagina)
    
    presupuesto.setStrokeColorRGB(0,0,0,0)
    presupuesto.setFillColor(HexColor('#0066f5'))
    presupuesto.rect(30, documento['alto_documento']-250, documento['ancho_documento']-80, 30, stroke=1, fill=1)
    
    y = documento['alto_documento'] - 240
    x1 = 50
    x2 = documento['ancho_documento']/2 - 10
    x3 = documento['ancho_documento'] - 130
    
    parrafo = Paragraph('Servicio', estilos['header_tabla'])
    width, height = parrafo.wrap(100, 100)
    parrafo.drawOn(presupuesto, 50, y)
    
    parrafo = Paragraph('Tiempo Estimado', estilos['header_tabla'])
    width, height = parrafo.wrap(200, 100)    
    parrafo.drawOn(presupuesto, x2, y)
    
    parrafo = Paragraph('Monto $', estilos['header_tabla'])
    width, height = parrafo.wrap(100, 100)
    parrafo.drawOn(presupuesto, x3, y)
    
    for servicio in datos_servicios:
        
        y -= 30
                
        parrafo = Paragraph(servicio, estilos['fila_tabla'])
        width, height = parrafo.wrap(300, 100)
        parrafo.drawOn(presupuesto, x1, y)

        parrafo = Paragraph(datos_servicios[servicio]['tiempo'], estilos['fila_tabla'])
        width, height = parrafo.wrap(200, 100)
        parrafo.drawOn(presupuesto, x2, y)

        parrafo = Paragraph(str(datos_servicios[servicio]['precio']), estilos['fila_tabla'])
        width, height = parrafo.wrap(100, 100)
        parrafo.drawOn(presupuesto, x3, y)
        
    y -= 30
    
    parrafo = Paragraph('Total', estilos['titulo_servicio'])
    width, height = parrafo.wrap(100, 100)
    parrafo.drawOn(presupuesto, x1, y)
    
    total = calcularTotal(datos_servicios)
    
    parrafo = Paragraph(f"${total}", estilos['titulo_servicio'])
    width, height = parrafo.wrap(100, 100)
    parrafo.drawOn(presupuesto, x3, y)
    
    
def calcularTotal(servicios):
    
    suma = 0
    
    for servicio in servicios:
        suma += servicios[servicio]['precio']
        
    return suma