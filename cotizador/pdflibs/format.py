import os
from datetime import date
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.fonts import addMapping
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle


base = os.getcwd()

def setDocumentProperties(hoja, fuente, numero_documento):
  
    documento = {}

    fecha = date.today()
    dia = fecha.day
    mes = getMonth(fecha.month)
    anio = fecha.year

    if hoja == 'carta':
        documento = {
            'ancho_documento': LETTER[0],
            'alto_documento': LETTER[1],
            'folio': f"Presupuesto N°{numero_documento}<br/>{dia} de {mes}, {anio}"
            }

    setFonts(fuente)
    estilos = setParagraphStyles()

    return documento, estilos


def setFonts(fuente):

    if fuente == 'Poppins': 
        rutas_fuentes = {
            'regular': base+'\\pdflibs\\fonts\\Poppins-Regular.ttf',
            'bold': base+'/pdflibs/fonts/Poppins-Bold.ttf',
            'light': base+'/pdflibs/fonts/Poppins-Light.ttf',
            'black': base+'/pdflibs/fonts/Poppins-Black.ttf',
            'xbold': base+'/pdflibs/fonts/Poppins-ExtraBold.ttf'
        }

        pdfmetrics.registerFont(TTFont('Poppins', rutas_fuentes['regular']))
        pdfmetrics.registerFont(TTFont('PoppinsBd', rutas_fuentes['bold']))
        pdfmetrics.registerFont(TTFont('PoppinsLi', rutas_fuentes['light']))
        pdfmetrics.registerFont(TTFont('PoppinsBl', rutas_fuentes['black']))
        pdfmetrics.registerFont(TTFont('PoppinsXb', rutas_fuentes['xbold']))

        addMapping('Poppins', 0, 0, 'Poppins')
        addMapping('Poppins', 1, 0, 'PoppinsBd')


def setParagraphStyles():

    title_fstyle = 'PoppinsBd'
    body_fstyle = 'Poppins'
    title_fsize = 16
    body_fsize = 9
    black_fcolor = HexColor('#000000')
    blue_fcolor = HexColor('#0066f5')
    yellow_fcolor = HexColor('#FEEB16')
    gray_fcolor = HexColor('#777777')
    white_fcolor = HexColor('#FFFFFF')

    # EN ESTA PARTE SE EDITAN LOS ESTILOS DE LA TIPOGRAFÍA
    estilos = {
        'titulo_presentacion': ParagraphStyle('title', fontName="PoppinsBd", fontSize=title_fsize, spaceAfter=14, textColor=blue_fcolor),
        'body_presentacion': ParagraphStyle('body', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=gray_fcolor),
        'firma_presentacion': ParagraphStyle('body', fontName="PoppinsBd", fontSize=body_fsize, spaceAfter=14, textColor=gray_fcolor),
        'contacto_presentacion': ParagraphStyle('body', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=gray_fcolor),
        'header_fecha': ParagraphStyle('header', fontName="PoppinsBd", fontSize=body_fsize, spaceAfter=14, textColor=blue_fcolor),
        'contacto_servicios': ParagraphStyle('header', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=blue_fcolor),
        'header_datos_cliente': ParagraphStyle('header', fontName="PoppinsBd", fontSize=body_fsize, spaceAfter=14, textColor=black_fcolor),
        'datos_cliente': ParagraphStyle('header', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=black_fcolor),
        'titulo_servicio': ParagraphStyle('title', fontName="PoppinsBd", fontSize=title_fsize, spaceAfter=14, textColor=blue_fcolor),
        'body_servicios': ParagraphStyle('body', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=black_fcolor),
        'header_tabla': ParagraphStyle('title', fontName="PoppinsBd", fontSize=13, spaceAfter=14, textColor=white_fcolor),
        'fila_tabla': ParagraphStyle('body', fontName="Poppins", fontSize=11, spaceAfter=14, textColor=gray_fcolor),
    }

    return estilos


def getMonth(mes):
    if mes == 1:
        return 'enero'
    elif mes == 2:
        return 'febrero'
    elif mes == 3:
        return 'marzo'
    elif mes == 4:
        return 'abril'
    elif mes == 5:
        return 'mayo'
    elif mes == 6:
        return 'junio'
    elif mes == 7:
        return 'julio'
    elif mes == 8:
        return 'agosto'
    elif mes == 9:
        return 'septiembre'
    elif mes == 10:
        return 'octubre'
    elif mes == 11:
        return 'noviembre'
    else:
        return 'diciembre'