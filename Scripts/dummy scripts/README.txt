En caso que se necesite generar información dummy, estos o son los
siguientes pasos:

0. Asegúrese que dummy.py y randomnames.csv se encuentran en el directorio.

1. python dummy.py (en caso de ser necesario)

2. Crear la base de datos satdb previamente y haber creado las tablas iniciales,
para más información utiliza el script de setup.sh.
	2.1 mysql -u root -p < dummy_nombres.sql
	2.2 mysql -u root -p < dummy_clases.sql
	2.3 mysql -u root -p < dummy_grupos.sql
	2.4 mysql -u root -p < dummy_inscritos.sql
