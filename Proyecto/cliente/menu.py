def menu(mostrar_diagrama):
    print("\n¿Qué tarea desea realizar?")
    print("1. Sumar dos números")
    print("2. Convertir grados Celsius a Fahrenheit")
    print("3. Determinar si un número es par o impar")
    print("4. Ver diagrama de arquitectura")
    print("5. Salir")
    while True:
        opcion = input("Elija una opción (1-5): ")
        if opcion == "1":
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            return f"sumar,{a},{b}"
        elif opcion == "2":
            c = float(input("Ingrese los grados Celsius: "))
            return f"celsius_a_fahrenheit,{c}"
        elif opcion == "3":
            n = int(input("Ingrese el número: "))
            return f"es_par,{n}"
        elif opcion == "4":
            mostrar_diagrama()
            return None
        elif opcion == "5":
            print("Saliendo del programa. Hasta luego.")
            exit(0)
        else:
            print("Opción inválida. Intente nuevamente o presione '5' para salir.")
