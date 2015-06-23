# -*- coding: utf-8 -*-
import subprocess, os
import time
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import flowables

# Obtiene la fecha en formato numero_de_dia de mes de año
def obten_fecha():
    dia = time.strftime("%d")
    mes = convierte_mes(time.strftime("%m"))
    anio = time.strftime("%Y")
    return dia + " de " + mes + " del " + anio

# Obtiene la fecha en formato dia_de_semana numero_de_dia de mes de año
def obten_fecha_completa():
    nombre_dia = convierte_dia(time.strftime("%A"))
    return nombre_dia + " " + obten_fecha()

# Convierte el numero de mes en texto en español
def convierte_mes(mes):
    if mes == "01":
        return "Enero"
    elif mes == "02":
        return "Febrero"
    elif mes == "03":
        return "Marzo"
    elif mes == "04":
        return "Abril"
    elif mes == "05":
        return "Mayo"
    elif mes == "06":
        return "Junio"
    elif mes == "07":
        return "Julio"
    elif mes == "08":
        return "Agosto"
    elif mes == "09":
        return "Septiembre"
    elif mes == "10":
        return "Octubre"
    elif mes == "11":
        return "Noviembre"
    elif mes == "12":
        return "Diciembre"

# Traductor del dia de la semana de español a ingles
def convierte_dia(dia):
    if dia == "Monday":
        return "LUNES"
    elif dia == "Tuesday":
        return "MARTES"
    elif dia == "Wednesday":
        return "MIERCOLES"
    elif dia == "Thursday":
        return "JUEVES"
    elif dia == "Friday":
        return "VIERNES"
    elif dia == "Saturday":
        return "SABADO"
    elif dia == "Sunday":
        return "DOMINGO"

# Crea una de las cartas, con la información de un alumno
def primera_carta(materia, salon, horario, nombres, apellidos, matricula, tipo_seleccion, fecha, fecha_completa, styles, imagen):
    nombre_escritor = "Ing. Jorge Cervantes Oviedo"
    cargo_escritor = "Director"
    departamento = "Departamente de Prevención de Adicciones en el Tec"
    campus = "Campus Monterrey"
    calle_campus = "Eugenio Garza Sada 2501"
    direccion_campus = "64849, Monterrey, N.L., México"
    telefono = "Tel: " + "52/81 8358 2000"
    nombre_alumno = nombres + " " + apellidos
    salon_horario = salon + "    " + horario
    
    # Hoja donde se vacia la información
    hoja=[]
    
    hoja.append(imagen)
    texto = '<b><font size=12>%s<br/><br/>%s<br/>%s<br/>%s<br/>%s</font></b>' % (fecha, materia, salon_horario, nombre_alumno, matricula)
    hoja.append(Paragraph(texto, styles["Right"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12>CARTA NOTIFICACIÓN</font>'
    hoja.append(Paragraph(texto, styles["Center"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12>Una de las acciones permanentes del Tecnológico de Monterrey Campus Monterrey y el Departamento de Prevención de las Adicciones CAT es la de llevar a cabo pruebas antidoping entre nuestros estudiantes, con la finalidad de desalentar el consumo de sustancias prohibidas entre la comunidad estudiantil.</font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 12))

    texto = '<font size=12>En esta ocasión fuiste <b>%s</b>, muchas gracias por colaborar para lograr nuestro objetivo de mantener nuestra comunidad académica libre de adicciones y ayudar a aquellas personas que tengan algún tipo de consumo de sustancias ilegales.</font>' %tipo_seleccion
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 12))

    texto = '<font size=12>Te pido que te presentes el día de <b>HOY en las oficinas del CAT, ubicada en Centrales DC-201 segundo piso, por el Domo Acuático.</b></font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12><b><u>HOY %s</u> de 9:00a.m. A 1:00p.m. ó 3:00 a 5:00p.m.</b></font>' %fecha_completa
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 12))

    texto = '<font size=12><b>NO OLVIDES TRAER TU CREDENCIAL.</b></font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 12))

    texto = '<font size=12><b>TU ASISTENCIA ES OBLIGATORIA</b> acorde al Reglamento General de Alumnos vigente.</font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 48))

    texto = '<font size=12>Atentamente,</font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 36))

    texto = '<font size=12>%s<br/>%s<br/>%s<br/>%s<br/></font>' %(nombre_escritor, cargo_escritor, departamento, campus)
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 48))

    texto = '<font size=10 color="gray">%s<br/>%s<br/>%s<br/>%s<br/></font>' %(campus, calle_campus, direccion_campus, telefono)
    hoja.append(Paragraph(texto, styles["Right"]))
    hoja.append(PageBreak())
    
    return hoja

# Crea una de las cartas, con la información de un alumno
def segunda_carta(materia, salon, horario, nombres, apellidos, matricula, tipo_seleccion, fecha, fecha_completa, styles, imagen):
    nombre_escritor = "Ing. Jorge Cervantes Oviedo"
    cargo_escritor = "Director"
    departamento = "Departamente de Prevención de Adicciones en el Tec"
    campus = "Campus Monterrey"
    calle_campus = "Eugenio Garza Sada 2501"
    direccion_campus = "64849, Monterrey, N.L., México"
    telefono = "Tel: " + "52/81 8358 2000"
    nombre_alumno = nombres + " " + apellidos
    salon_horario = salon + "    " + horario
    
    # Hoja donde se vacia la información
    hoja=[]
    
    hoja.append(imagen)
    texto = '<b><font size=12>%s<br/><br/>%s<br/>%s<br/>%s<br/>%s</font></b>' % (fecha, materia, salon_horario, nombre_alumno, matricula)
    hoja.append(Paragraph(texto, styles["Right"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12>SEGUNDA CARTA NOTIFICACIÓN</font>'
    hoja.append(Paragraph(texto, styles["Center"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12>Atentamente,</font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 36))

    texto = '<font size=12>%s<br/>%s<br/>%s<br/>%s<br/></font>' %(nombre_escritor, cargo_escritor, departamento, campus)
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 48))

    hoja.append(Spacer(1, 264))

    texto = '<font size=10 color="gray">%s<br/>%s<br/>%s<br/>%s<br/></font>' %(campus, calle_campus, direccion_campus, telefono)
    hoja.append(Paragraph(texto, styles["Right"]))

    hoja.append(PageBreak())
    
    return hoja

# Crea una de las cartas, con la información de un alumno
def tercera_carta(materia, salon, horario, nombres, apellidos, matricula, tipo_seleccion, fecha, fecha_completa, styles, imagen):
    nombre_escritor = "Ing. Jorge Cervantes Oviedo"
    cargo_escritor = "Director"
    departamento = "Departamente de Prevención de Adicciones en el Tec"
    campus = "Campus Monterrey"
    calle_campus = "Eugenio Garza Sada 2501"
    direccion_campus = "64849, Monterrey, N.L., México"
    telefono = "Tel: " + "52/81 8358 2000"
    nombre_alumno = nombres + " " + apellidos
    salon_horario = salon + "    " + horario
    
    # Hoja donde se vacia la información
    hoja=[]
    
    hoja.append(imagen)
    texto = '<b><font size=12>%s<br/><br/>%s<br/>%s<br/>%s<br/>%s</font></b>' % (fecha, materia, salon_horario, nombre_alumno, matricula)
    hoja.append(Paragraph(texto, styles["Right"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12>SEGUNDA CARTA NOTIFICACIÓN</font>'
    hoja.append(Paragraph(texto, styles["Center"]))
    hoja.append(Spacer(1, 24))

    texto = '<font size=12>Atentamente,</font>'
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 36))

    texto = '<font size=12>%s<br/>%s<br/>%s<br/>%s<br/></font>' %(nombre_escritor, cargo_escritor, departamento, campus)
    hoja.append(Paragraph(texto, styles["Justify"]))
    hoja.append(Spacer(1, 48))

    hoja.append(Spacer(1, 264))

    texto = '<font size=10 color="gray">%s<br/>%s<br/>%s<br/>%s<br/></font>' %(campus, calle_campus, direccion_campus, telefono)
    hoja.append(Paragraph(texto, styles["Right"]))

    hoja.append(PageBreak())
    
    return hoja