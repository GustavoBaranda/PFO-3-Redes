
#!/usr/bin/env bash

cd "$(dirname "$BASH_SOURCE")" || exit 1

VENV_DIR="../PFO3_ENV"
REQ_FILE="requirements.txt"

echo "Iniciando proceso..."

if command -v py >/dev/null 2>&1; then
    PY_CMD="py -3"
elif command -v python3 >/dev/null 2>&1; then
    PY_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PY_CMD="python"
else
    echo "No se encontró Python 3 en PATH. Instale Python y vuelva a intentar." >&2
    exit 1
fi

CREATED=false
if [ ! -d "$VENV_DIR" ]; then
    echo "Creando virtualenv en $VENV_DIR..."
    $PY_CMD -m venv "$VENV_DIR"
    CREATED=true
else
    echo "El virtualenv ya existe; se omite la creación."
fi

if [ -f "$VENV_DIR/Scripts/activate" ]; then
    source "$VENV_DIR/Scripts/activate"
    PY_BIN="$VENV_DIR/Scripts/python"
elif [ -f "$VENV_DIR/bin/activate" ]; then
    source "$VENV_DIR/bin/activate"
    PY_BIN="$VENV_DIR/bin/python"
else
    echo "No encontré activate del venv, fijate la ruta." >&2
    exit 1
fi

if [ "$CREATED" = true ] && [ -f "$REQ_FILE" ]; then

    echo "Actualizando pip, setuptools y wheel en el venv..."
    "${PY_BIN}" -m pip install --upgrade pip setuptools wheel || \
        echo "Advertencia: fallo al actualizar pip (continúo con la instalación)..."

    echo "Instalando dependencias desde $REQ_FILE..."
    "${PY_BIN}" -m pip install -r "$REQ_FILE"
else
    echo "No se instalarán dependencias (venv existente o requirements ausente)."
fi

echo "Iniciando servidor en segundo plano..."
"${PY_BIN}" ./servidor.py &
PID=$!
echo "Servidor iniciado (PID: $PID)"

cleanup()
{
    if [ -n "$PID" ]; then
        echo "Interrupción detectada: matando servidor (PID: $PID)..."
        kill "$PID" 2>/dev/null || true
        wait "$PID" 2>/dev/null || true
    fi
    exit 130
}

trap 'cleanup' INT TERM

sleep 1

echo "Iniciando cliente..."
"${PY_BIN}" ./cliente.py || echo "El cliente finalizó con error."

echo "El servidor continúa en segundo plano (PID: $PID)."
echo "Para detenerlo: kill $PID"
