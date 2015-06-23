# -*- coding: utf-8 -*
from django import template
import datetime

register = template.Library()

def horario(inscrito, dia):
    if dia == "lunes":
        return inscrito.grupo.horario_1
    elif dia == "martes":
        return inscrito.grupo.horario_2
    elif dia == "miercoles":
        return inscrito.grupo.horario_3
    elif dia == "jueves":
        return inscrito.grupo.horario_4
    elif dia == "viernes":
        return inscrito.grupo.horario_5
    elif dia == "sabado":
        return inscrito.grupo.horario_6 

def estado(estado_en_numero):
    # print estado_en_numero
    # print estado_en_numero == 0
    if estado_en_numero == 0:
        return 'Iniciado'
    elif estado_en_numero == 1:
        return '1era. Noticificación recibida'
    elif estado_en_numero == 2:
        return '2da. Noticificación recibida'
    elif estado_en_numero == 3:
        return 'Encuesta realizada'
    elif estado_en_numero == 4:
        return 'Prueba realizada'
    elif estado_en_numero == 5:
        return 'Cerrado'

def color(color_en_numero):
    if color_en_numero == 0:
        return '#8CBF26'  #VERDE
    elif color_en_numero == 1:
        return '#E8BE1B'  #AMARILLO
    elif color_en_numero == 2:
        return '#F09609'  #NARANJA
    elif color_en_numero == 3:
        return '#E51400'  #ROJO
    elif color_en_numero == 4:
        return '#000000'  #NEGRO
    else:
        return '#989898'

def color_texto(color_en_numero):
    if color_en_numero == 0:
        return 'Verde'  #VERDE
    elif color_en_numero == 1:
        return 'Amarillo'  #AMARILLO
    elif color_en_numero == 2:
        return 'Naranja'  #NARANJA
    elif color_en_numero == 3:
        return 'Rojo'  #ROJO
    elif color_en_numero == 4:
        return 'Negro'  #NEGRO
    else:
        return 'No encontrado'

def resultado(resultado_en_numero):
    if resultado_en_numero == 0:
        return 'Negativo' 
    elif resultado_en_numero == 1:
        return 'Positivo'  
        
register.filter('estado', estado)
register.filter('horario', horario)
register.filter('color', color)
register.filter('color_texto', color_texto)
register.filter('resultado', resultado)