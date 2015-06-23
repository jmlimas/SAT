from horario import convierte_de_horario, obtener_horario_de_forma

pruebas = [
['10+/3|A-A3-301','|', True],
['10|A4', '|', True], 
['10/|A4', '|', None], 
['10/a|A4', '|', None], 
['10+|A4', '|', True],
['10|', '|', True],
]

for prueba in pruebas:
	print "Probando.. %s Delim.. %s" % (prueba[0], prueba[1])
	h = convierte_de_horario(prueba[0], prueba[1], debug=True)
	if h is not None:
		print h
		h = True
	else:
		print 'Horario en formato incorrecto.'
	print h == prueba[2]
	print ''
	
print obtener_horario_de_forma('7', '8+')
print obtener_horario_de_forma('8+', '7')
	# print "\n"
