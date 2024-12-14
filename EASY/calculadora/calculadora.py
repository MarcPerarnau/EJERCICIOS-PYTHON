def calculadora():
    print("Bienvenido a la calculadora")
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("\nSelecciona una opción (1-5): "))
            
            if opcion == 5:
                print("Saliendo de la calculadora. ¡Hasta luego!")
                break

            if opcion not in [1, 2, 3, 4]:
                print("Por favor, selecciona una opción válida.")
                continue

            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == 2:
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == 3:
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == 4:
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")

        except ValueError:
            print("Por favor, ingresa un número válido.")

# Llamar a la función
calculadora()
