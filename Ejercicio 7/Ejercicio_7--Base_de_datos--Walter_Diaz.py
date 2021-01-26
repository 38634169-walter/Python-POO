import mysql.connector

usuarios = [("Pedro","riobambam"),("Jose","remembering"),("Rosario","truncateitbitch"),("Rodrigo","playharder"),("Cristian","getacomplished")]

conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "wally 2567",
    database = "fablab"
    )

micursor = conexion.cursor()

micursor.execute("""

SELECT *
FROM usuario JOIN cursos
ON usuario.usuario = cursos.usuario;



""")

print(micursor.fetchall())
conexion.close()
