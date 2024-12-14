import tkinter as tk
import random
import string

def generar_contrasena():
    longitud = int(entry_longitud.get())
    incluir_mayusculas = var_mayusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()

    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    etiqueta_resultado.config(text=f"Contraseña generada: {contrasena}")

# Configuración de la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Entradas y etiquetas
etiqueta_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
etiqueta_longitud.pack()

entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

var_mayusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

checkbox_mayusculas = tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayusculas)
checkbox_mayusculas.pack()

checkbox_numeros = tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros)
checkbox_numeros.pack()

checkbox_simbolos = tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos)
checkbox_simbolos.pack()

boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contrasena)
boton_generar.pack()

etiqueta_resultado = tk.Label(ventana, text="Contraseña generada: ")
etiqueta_resultado.pack()

# Ejecutar la interfaz
ventana.mainloop()
