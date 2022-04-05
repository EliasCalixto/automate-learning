import sqlite3

miConexion=sqlite3.connect('darkesthj')

miCursor=miConexion.cursor()

# miCursor.execute('CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))')

miCursor.execute('INSERT INTO PRODUCTOS VALUES("BALON", 15, "DEPORTES")')



miConexion.commit()

miConexion.close()
