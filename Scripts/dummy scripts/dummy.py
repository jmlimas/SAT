# -*- coding: utf-8 -*-
# Autor: Raul Jimenez
# Email: jimenezjrs@gmail.com

def generate(
	matricula=80000, 
	nombre_sql_prefix = 'dummy_',
	nombre_sql_suffix = '.sql',
	archivo_con_nombres = 'randomnames.csv',
	base_de_datos = 'satdb',
	tabla_alumnos = 'app_estudiante',
	tabla_clases = 'app_clase',
	tabla_grupos = 'app_grupo',
	tabla_inscritos = 'app_inscrito',
	cantidad_de_alumnos = 0,
	cantidad_de_clases = 100,
	cantidad_de_grupos = 500
						):

	from random import randint, random, sample

	# Definición de funciones.
	def agregar_comentarios_iniciales(archivo):
		archivo.write("-- Archivo generado automaticamente\n")
		archivo.write("-- No modificar el archivo de forma manual\n")
		archivo.write("-- Autor: Raul Jimenez\n")
		archivo.write("-- Email: jimenezjrs@gmail.com\n\n")

	def generar_dummy_nombres(linea):
		palabras = linea.split(',')
		nombre = palabras[0].replace("'", "")
		apellido = palabras[1].replace("'", "")
		estado = randint(0,10)
		return nombre, apellido, estado

	def generar_dummy_clases(cantidad=100, prefijo_clave='TC', prefijo_nombre='Materia_'):
		rango = range(1, cantidad)
		# Regresa una lista con las claves y otra con nombres.
		claves_materia = map(lambda num: prefijo_clave + str(num) , rango)
		nombres_materia = map(lambda num: prefijo_nombre + str(num) , rango)
		return claves_materia, nombres_materia

	def generar_dummy_grupos(cantidad_de_grupos=500, crn_init=1000, cantidad_de_clases=100):

		def genera_hora():
			if random() <= .6:
				delimitador='|'
				horario = str(randint(7, 18)) + sample(['+', ''], 1)[0] + sample(['/3', '/6', ''], 1)[0]
				salon = sample(['A-A1-', 'A-A2-', 'A-A3-', 'A-A4-', 'A-A5-', 'CIAP-'], 1)[0] + str(randint(100, 500))
		
				dia = horario + delimitador + salon
				return dia
			else:
				return None

		# semana = map(lambda dia: genera_hora(), xrange(5))

		# crns = range(crn_init, cantidad)
		# clase = map(lambda iteracion: randint(0, cantidad_de_clases - 1), xrange(cantidad))

		grupos = map(lambda iteracion: {
			'crn': iteracion, 
			'clase': randint(1, cantidad_de_clases - 1), 
			'horario_1': genera_hora(),
			'horario_2': genera_hora(),
			'horario_3': genera_hora(),
			'horario_4': genera_hora(),
			'horario_5': genera_hora(),
			'profesor': 'John Doe'
			}, xrange(cantidad_de_grupos))
		return grupos


	# Vamos a abrir el archivo con nombres.
	archivo_con_nombres = open(archivo_con_nombres)

	# Creación del script de sql con información dummy.
	with open(nombre_sql_prefix + 'nombres' +nombre_sql_suffix, "w") as sql_output:
		# Agregar la base de datos que utilizaremos.
		agregar_comentarios_iniciales(sql_output)

		# Agregar la base de datos que utilizaremos.
		sql_output.write("USE %s;\n\n" % base_de_datos)

		# Iterar sobre el archivo de los nombres para obtener los nombres.
		sql_output.write("START TRANSACTION;\n")
		for linea in archivo_con_nombres:
			nombre, apellido, estado_actual = generar_dummy_nombres(linea)
			sql_output.write("INSERT INTO %s (matricula, nombre, apellido, color) " % tabla_alumnos)
			sql_output.write("VALUES (%d, \"%s\", \"%s\", %d);\n" % (matricula, nombre, apellido, estado_actual))
			matricula = matricula + 1
			cantidad_de_alumnos = cantidad_de_alumnos + 1
		sql_output.write("COMMIT;\n\n")
	
	with open(nombre_sql_prefix + 'clases' +nombre_sql_suffix, "w") as sql_output:
		# Agregar la base de datos que utilizaremos.
		agregar_comentarios_iniciales(sql_output)
		# Agregar la base de datos que utilizaremos.
		sql_output.write("USE %s;\n\n" % base_de_datos)

		# Crear las clases.
		sql_output.write("START TRANSACTION;\n")
		claves_materia, nombres_materia = generar_dummy_clases(cantidad_de_clases)
		for i in xrange(cantidad_de_clases-1):
			sql_output.write("INSERT INTO %s (clave_materia, nombre) VALUES(\"%s\", \"%s\");\n" % (tabla_clases,claves_materia[i], nombres_materia[i]))
		sql_output.write("COMMIT;\n\n")

	with open(nombre_sql_prefix + 'grupos' +nombre_sql_suffix, "w") as sql_output:
		# Agregar la base de datos que utilizaremos.
		agregar_comentarios_iniciales(sql_output)

		# Agregar la base de datos que utilizaremos.
		sql_output.write("USE %s;\n\n" % base_de_datos)

		grupos = generar_dummy_grupos(500, 1000, 100)
		sql_output.write("START TRANSACTION;\n")
		for grupo in grupos:
			sql_output.write("INSERT INTO %s (crn, clase_id, horario_1, horario_2, horario_3, horario_4, horario_5, profesor) " % tabla_grupos)
			sql_output.write("VALUES (%d, %d, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');\n" 
				% (grupo['crn'], grupo['clase'], grupo['horario_1'], grupo['horario_2'], grupo['horario_3'], grupo['horario_4'], grupo['horario_5'], grupo['profesor']))
		sql_output.write("COMMIT;\n\n")

	with open(nombre_sql_prefix + 'inscritos' +nombre_sql_suffix, "w") as sql_output:
		# Agregar la base de datos que utilizaremos.
		agregar_comentarios_iniciales(sql_output)

		# Agregar la base de datos que utilizaremos.
		sql_output.write("USE %s;\n\n" % base_de_datos)
		
		sql_output.write("START TRANSACTION;\n")
		for matricula in xrange(cantidad_de_alumnos):
			matricula = 80000 + matricula
			muestra = sample(grupos, 6)
			for inscrito in muestra:
				sql_output.write("INSERT INTO %s (estudiante_id, grupo_id) " % tabla_inscritos)
				sql_output.write("VALUES (%d, %d);\n" 
				% (matricula, inscrito['crn']))
		sql_output.write("COMMIT;\n\n")

		# Impresion de detalles de la muestra.
		print cantidad_de_alumnos, "alumnos dummy creados..."
		print cantidad_de_clases, "clases dummy creados..."
		print len(grupos), "grupos dummy creados..."


generate()

