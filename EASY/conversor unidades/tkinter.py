import tkinter as tk
from tkinter import ttk

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

def realizar_conversion():
    try:
        valor = float(entry_valor.get())
        categoria = categoria_combobox.get()
        de = unidad_origen_combobox.get()
        a = unidad_destino_combobox.get()
        
        if categoria == "Longitud":
            resultado = convertir_longitud(valor, de, a)
        elif categoria == "Masa":
            resultado = convertir_masa(valor, de, a)
        elif categoria == "Temperatura":
            resultado = convertir_temperatura(valor, de, a)
        
        label_resultado.config(text=f"Resultado: {resultado} {a}")
    except ValueError:
        label_resultado.config(text="Error: Ingrese un valor válido.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Conversor de Unidades")

# Entrada de valor
label_valor = tk.Label(ventana, text="Ingresa el valor:")
label_valor.pack()

entry_valor = tk.Entry(ventana)
entry_valor.pack()

# Selección de categoría
label_categoria = tk.Label(ventana, text="Selecciona la categoría:")
label_categoria.pack()

categoria_combobox = ttk.Combobox(ventana, values=["Longitud", "Masa", "Temperatura"])
categoria_combobox.pack()

# Selección de unidad de origen y destino
label_unidad_origen = tk.Label(ventana, text="Selecciona la unidad de origen:")
label_unidad_origen.pack()

unidad_origen_combobox = ttk.Combobox(ventana)
unidad_origen_combobox.pack()

label_unidad_destino = tk.Label(ventana, text="Selecciona la unidad de destino:")
label_unidad_destino.pack()

unidad_destino_combobox = ttk.Combobox(ventana)
unidad_destino_combobox.pack()

# Botón de conversión
boton_convertir = tk.Button(ventana, text="Convertir", command=realizar_conversion)
boton_convertir.pack()

# Resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar la aplicación
ventana.mainloop()
