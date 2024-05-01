import random

def opcion_1():
    print("Generando un número aleatorio del 1 al 100:")
    print(random.randint(1, 100))

def opcion_2():
    print("Realizando una operación matemática especial:")
    resultado = 7 * 5 + 10 / 2 - 3
    print("El resultado de la operación es:", resultado)

def mostrar_menu():
    print("\nMenu:")
    print("1. Generar número aleatorio")
    print("2. Realizar operación matemática especial")
    print("3. Salir")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
