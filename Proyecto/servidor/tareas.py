def sumar(a, b):
    return f"La suma de {a} y {b} es {a + b}"

def celsius_a_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f"{c} grados Celsius son {f} grados Fahrenheit"

def es_par(n):
    if n % 2 == 0:
        return f"El número {n} es par"
    else:
        return f"El número {n} es impar"
