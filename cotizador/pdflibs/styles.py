from reportlab.lib.styles import ParagraphStyle

def setParagraphStyles():

    title_fstyle = 'PoppinsBd'
    body_fstyle = 'Poppins'
    title_fsize = 16
    subtitle_fsize = 13
    body_fsize = 9
    black_fcolor = HexColor('#000000')
    blue_fcolor = HexColor('#0066f5')
    yellow_fcolor = HexColor('#FEEB16')
    gray_fcolor = HexColor('#777777')

    # EN ESTA PARTE SE EDITAN LOS ESTILOS DE LA TIPOGRAFÍA
    paragraph_styles = {
        'titulo_presentacion': ParagraphStyle('title', fontName="PoppinsBd", fontSize=title_fsize, spaceAfter=14, textColor=blue_fcolor),
        'body_presentacion': ParagraphStyle('body', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=gray_fcolor),
        'firma_presentacion': ParagraphStyle('body', fontName="PoppinsBd", fontSize=body_fsize, spaceAfter=14, textColor=gray_fcolor),
        'contacto_presentacion': ParagraphStyle('body', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=gray_fcolor),
        'header_fecha': ParagraphStyle('header', fontName="PoppinsBd", fontSize=body_fsize, spaceAfter=14, textColor=blue_fcolor),
        'header_datos_cliente': ParagraphStyle('header', fontName="PoppinsBd", fontSize=body_fsize, spaceAfter=14, textColor=black_fcolor),
        'datos_cliente': ParagraphStyle('header', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=black_fcolor),
        'titulo_servicio': ParagraphStyle('title', fontName="PoppinsBd", fontSize=title_fsize, spaceAfter=14, textColor=blue_fcolor),
        'titulo_subservicio': ParagraphStyle('title', fontName="PoppinsBd", fontSize=subtitle_fsize, spaceAfter=14, textColor=black_fcolor),
        'body_servicios': ParagraphStyle('body', fontName="Poppins", fontSize=body_fsize, spaceAfter=14, textColor=black_fcolor),
    }

    return paragraph_styles
