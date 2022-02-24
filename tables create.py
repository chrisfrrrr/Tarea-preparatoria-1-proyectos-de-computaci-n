import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="contraseña",
    database="proyectos",
    port="5432"
)

connection.autocommit = True
def creartabla():
    cursor = connection.cursor()
    query ="CREATE TABLE datos(nombre varchar(30),carnet varchar(100))"
    try:
        cursor.execute(query)
    except:
        print("la tabla ya existe")
    cursor. close()

creartabla()
