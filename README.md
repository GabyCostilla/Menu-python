# Programa de Python con Opciones 🐍

¡Bienvenido a este simple programa de Python con opciones! Este programa te permite elegir entre varias opciones y realizar diferentes acciones. A continuación, se detallan las opciones disponibles:

## Opciones Disponibles 🎮

1. **Generar Número Aleatorio**: Esta opción generará un número aleatorio entre 1 y 100.
2. **Realizar Operación Matemática Especial**: Esta opción realizará una operación matemática especial (7 * 5 + 10 / 2 - 3).

## Cómo Utilizar 🚀

1. Ejecuta el programa en tu entorno de Python.
2. Selecciona una opción del menú presentado.
3. El programa ejecutará la acción asociada a la opción seleccionada.
4. Si deseas salir del programa, selecciona la opción "3".

## Ejemplo de Uso 💡

```python
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
