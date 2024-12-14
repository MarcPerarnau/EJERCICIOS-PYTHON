def convertir_longitud(valor, de, a):
    conversiones = {
        "metros": 1.0,
        "kilometros": 1000.0,
        "millas": 1609.34,
        "yardas": 0.9144
    }
    return valor * conversiones[a] / conversiones[de]

def convertir_masa(valor, de, a):
    conversiones = {
        "gramos": 1.0,
        "kilogramos": 1000.0,
        "libras": 453.592,
        "onzas": 28.3495
    }
    return valor * conversiones[a] / conversiones[de]

def convertir_temperatura(valor, de, a):
    if de == "Celsius" and a == "Fahrenheit":
        return valor * 9 / 5 + 32
    elif de == "Fahrenheit" and a == "Celsius":
        return (valor - 32) * 5 / 9
    elif de == "Celsius" and a == "Kelvin":
        return valor + 273.15
    elif de == "Kelvin" and a == "Celsius":
        return valor - 273.15
    elif de == "Fahrenheit" and a == "Kelvin":
        return (valor - 32) * 5 / 9 + 273.15
    elif de == "Kelvin" and a == "Fahrenheit":
        return (valor - 273.15) * 9 / 5 + 32
    else:
        return valor

def mostrar_menu():
    print("Bienvenido al Conversor de Unidades")
    print("Seleccione la categoría:")
    print("1. Longitud")
    print("2. Masa")
    print("3. Temperatura")
    
    try:
        categoria = int(input("Ingrese el número de la categoría: "))
        if categoria not in [1, 2, 3]:
            print("Opción no válida")
            return

        valor = float(input("Ingrese el valor a convertir: "))
        
        if categoria == 1:
            print("Seleccione las unidades de Longitud: metros, kilometros, millas, yardas")
            de = input("De: ").lower()
            a = input("A: ").lower()
            if de not in ["metros", "kilometros", "millas", "yardas"] or a not in ["metros", "kilometros", "millas", "yardas"]:
                print("Unidad no válida")
                return
            resultado = convertir_longitud(valor, de, a)
            print(f"Resultado: {resultado} {a}")
        
        elif categoria == 2:
            print("Seleccione las unidades de Masa: gramos, kilogramos, libras, onzas")
            de = input("De: ").lower()
            a = input("A: ").lower()
            if de not in ["gramos", "kilogramos", "libras", "onzas"] or a not in ["gramos", "kilogramos", "libras", "onzas"]:
                print("Unidad no válida")
                return
            resultado = convertir_masa(valor, de, a)
            print(f"Resultado: {resultado} {a}")
        
        elif categoria == 3:
            print("Seleccione las unidades de Temperatura: Celsius, Fahrenheit, Kelvin")
            de = input("De: ").capitalize()
            a = input("A: ").capitalize()
            if de not in ["Celsius", "Fahrenheit", "Kelvin"] or a not in ["Celsius", "Fahrenheit", "Kelvin"]:
                print("Unidad no válida")
                return
            resultado = convertir_temperatura(valor, de, a)
            print(f"Resultado: {resultado} {a}")
    
    except ValueError:
        print("Error: Ingrese un valor válido.")

# Ejecutar el conversor
mostrar_menu()
