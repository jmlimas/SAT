#!/bin/bash
#
# Script de Instalación del Sistema Antidoping
#
# Escrito por Raúl Jiménez <jimenezjrs@gmail.com>
# 
# Notas: Para evitar problemas, corre el archivo como sudo.


# Edita la contraseña por la que diste de alta cuando instalaste mysql.
db_user=root
db_password=

echo "Escoge una de las opciones" 
echo "   1. Instalar Django."
echo "   2. Instalar MySQL."
echo "   3. Crear usuario del SAT en MySQL"
# echo "   4. Instalar el SAT."
# echo "   5. Todo lo anterior."

echo ""
read -p "Opción: " opcion
echo $opcion
echo ""

case $opcion in
	1) 
	echo "Instalando Django..."
	wget -O Django-1.4.5.tar.gz "https://www.djangoproject.com/download/1.4.5/tarball/"
	tar xzvf Django-1.4.5.tar.gz
	cd Django-1.4.5
	sudo python setup.py install
	cd ..
	rm Django-1.4.5.tar.gz
	rm -r Django-1.4.5
	;;
	
	2) echo "Instalando MySQL..."
	sudo apt-get install mysql-server
	;;

	3) echo "Creando base de datos en MySQL..."
	echo "Creando usuario MySQL..."
	mysql --user=$db_user --password=$db_password < mysql_setup.sql
	;;
	
	# 4) echo "Instalando el SAT..." ;;
	# 5) echo "Instalando todo..." ;;
	*) echo "No existe esa opción, vuelve a correr el script...";;
esac
