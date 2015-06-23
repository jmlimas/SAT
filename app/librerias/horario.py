
# Implementar cuando la hora es unicamente 10 y una clase comienza a las 10+.
def convierte_de_horario(horario_salon, delimitador, debug=False):
	import sys
	try:	
		# El horario puede venir de la siguiente forma: hora (arg0) (delimitador) salon (arg1).
		argumentos = horario_salon.split(delimitador)
		salon = argumentos[1]
		
		# El horario tec puede ser de la siguiente forma 10+/3.
		horario_tec = argumentos[0]

		if '+' in horario_tec:
			inicia_en_minuto = 0.5				# Comienza a mitad de hora.
	 	else:
	 		inicia_en_minuto = 0

	 	horario_tec = horario_tec.replace('+', '')

	 	# Quiere decir que la duracion se maneja en media horas.
	 	if '/' in horario_tec:
	 		tiempo = horario_tec.split('/')
			hora_inicio = int(tiempo[0])
			duracion = int(tiempo[1]) / 2.00			# Duracion en minutos.
		else:
			hora_inicio = int(horario_tec)
			duracion = 1.00

		hora_inicio = hora_inicio + inicia_en_minuto
		hora_fin = hora_inicio + duracion
		# Duracion en minutos.
		return {'hora_inicio': hora_inicio, 'hora_fin': hora_fin, 'salon': salon}

	except:
		if debug:
			print sys.exc_info()[0]
		return None

# convierte a horario ej. tiempo_inicio=8, timepo_fin 9+
def obtener_horario_de_forma(tiempo_inicio, tiempo_fin):
	import sys
	try:
		inicia_en_minuto = 0
		termina_en_minuto = 0

		# print tiempo_inicio, tiempo_fin
		if '+' in tiempo_inicio:
			inicia_en_minuto = .5
			tiempo_inicio = tiempo_inicio.replace('+', '')

		if '+' in tiempo_fin:
			termina_en_minuto = .5
			tiempo_fin = tiempo_fin.replace('+', '')

		# print tiempo_inicio, tiempo_fin
		hora_inicio = int(tiempo_inicio) + inicia_en_minuto
		hora_fin = int(tiempo_fin) + termina_en_minuto
		if hora_fin > hora_inicio:
			return {'hora_inicio': hora_inicio, 'hora_fin': hora_fin}
		return {'hora_inicio': hora_fin, 'hora_fin': hora_inicio}
	except:
		print sys.exc_info()[0]
		return None




