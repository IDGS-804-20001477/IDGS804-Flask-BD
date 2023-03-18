from db import get_connection

try:
    connection=get_connection
    with connection.cursor() as cursor:
        cursor.execute('call SP_CONSULTA_ALUMNO')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    print(ex)


try:
    connection=get_connection
    with connection.cursor() as cursor:
        cursor.execute('call SP_INSERTAR_ALUMNOS')
        connection.commit()
        connection.close()
except Exception as ex:
    print(ex)