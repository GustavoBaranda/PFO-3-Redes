from servidor.db.db import guardar_en_db
from servidor.tareas import sumar, celsius_a_fahrenheit, es_par

def worker(conn, addr):
    try:
        datos = conn.recv(1024).decode()
        partes = datos.split(',')
        tarea = partes[0]
        if tarea == "sumar":
            resultado = sumar(int(partes[1]), int(partes[2]))
        elif tarea == "celsius_a_fahrenheit":
            resultado = celsius_a_fahrenheit(float(partes[1]))
        elif tarea == "es_par":
            resultado = es_par(int(partes[1]))
        else:
            resultado = "Tarea desconocida"
        # Guardar en la base de datos
        guardar_en_db(tarea, ','.join(partes[1:]), resultado)
        conn.send(resultado.encode())
    except Exception as e:
        conn.send(f"Error: {e}".encode())
    finally:
        conn.close()
