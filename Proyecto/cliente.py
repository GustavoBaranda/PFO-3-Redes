
import socket
from cliente.menu import menu
from cliente.diagrama import mostrar_diagrama

# Cliente principal
def main():
    host = "127.0.0.1"
    # Leer el puerto desde la base de datos SQLite generada por el servidor
    try:
        import sqlite3
        conn_db = sqlite3.connect("tareas.db")
        cursor = conn_db.cursor()
        cursor.execute("SELECT valor FROM config WHERE clave = ?", ("puerto",))
        row = cursor.fetchone()
        if row:
            puerto = int(row[0])
        else:
            puerto = 5000
        conn_db.close()
    except Exception:
        puerto = 5000
    while True:
        tarea = menu(mostrar_diagrama)
        if tarea:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
                try:
                    cliente.connect((host, puerto))
                    cliente.send(tarea.encode())
                    resultado = cliente.recv(1024).decode()
                    print(f"Resultado: {resultado}")
                except Exception as e:
                    print(f"Error de conexión: {e}")
        seguir = None
        while True:
            seguir = input("¿Desea realizar otra tarea? (s/n): ").lower()
            if seguir == "n":
                print("Hasta luego.")
                return
            elif seguir == "s":
                break
            else:
                print("Respuesta inválida. Ingrese 's' para continuar o 'n' para salir.")
        # Si llegamos aquí, el usuario respondió 's' y el bucle continúa

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCerrando el programa...")
