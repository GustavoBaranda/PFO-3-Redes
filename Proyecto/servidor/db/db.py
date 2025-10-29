import sqlite3

def guardar_en_db(tarea, datos, resultado):
    conn_db = sqlite3.connect("tareas.db")
    cursor = conn_db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarea TEXT,
            datos TEXT,
            resultado TEXT
        )
    """)
    cursor.execute("INSERT INTO tareas (tarea, datos, resultado) VALUES (?, ?, ?)", (tarea, datos, resultado))
    conn_db.commit()
    conn_db.close()

def guardar_puerto(puerto):
    conn_db = sqlite3.connect("tareas.db")
    cursor = conn_db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            clave TEXT PRIMARY KEY,
            valor TEXT
        )
    """)
    cursor.execute("REPLACE INTO config (clave, valor) VALUES (?, ?)", ("puerto", str(puerto)))
    conn_db.commit()
    conn_db.close()
