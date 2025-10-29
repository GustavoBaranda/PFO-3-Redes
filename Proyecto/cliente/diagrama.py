import os
from plantuml import PlantUML
import webbrowser

def mostrar_diagrama():
    try:
        from PIL import Image
    except ImportError:
        Image = None
    ruta = os.path.join(os.path.dirname(__file__), "../Diagrama", "diagram.puml")
    salida = os.path.join(os.path.dirname(__file__), "../Diagrama", "diagram.png")

    def _unique_path(path):
        base, ext = os.path.splitext(path)
        if not os.path.exists(path):
            return path
        counter = 1
        while True:
            candidate = f"{base}-{counter}{ext}"
            if not os.path.exists(candidate):
                return candidate
            counter += 1

    salida = _unique_path(salida)
    try:
        try:
            from servidor.db.db import guardar_en_db
        except Exception:
            guardar_en_db = None

        server = PlantUML(url='http://www.plantuml.com/plantuml/img/')
        server.processes_file(ruta, salida)
        print("Imagen generada: " + salida)

        if guardar_en_db:
            try:
                guardar_en_db("generar_diagrama", ruta, salida)
            except Exception as e:
                print(f"No se pudo registrar en la DB: {e}")

        webbrowser.open('file://' + os.path.abspath(salida))
    except Exception as e:
        print(f"No se pudo mostrar el diagrama: {e}")
