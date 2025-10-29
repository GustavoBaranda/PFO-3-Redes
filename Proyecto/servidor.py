import socket
import threading
from servidor.db.db import guardar_puerto
from servidor.worker import worker

def main():
    host = "127.0.0.1"
    puerto = 5000
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            servidor.bind((host, puerto))
            break
        except OSError as e:
            if e.errno == 10048:
                print(f"Puerto {puerto} ocupado, probando el siguiente...")
                puerto += 1
            else:
                raise
    servidor.listen()
    print(f"Servidor escuchando en {host}:{puerto}")
    # Guardar el puerto en la base de datos SQLite
    guardar_puerto(puerto)
    while True:
        conn, addr = servidor.accept()
        hilo = threading.Thread(target=worker, args=(conn, addr))
        hilo.start()

if __name__ == "__main__":
    main()
