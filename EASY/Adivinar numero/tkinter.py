import tkinter as tk
import random

def adivinar_numero():
    global numero_objetivo, intentos
    
    adivinanza = int(entry.get())
    intentos += 1
    
    if adivinanza < numero_objetivo:
        resultado.config(text=f"El número es mayor. Intentos: {intentos}")
    elif adivinanza > numero_objetivo:
        resultado.config(text=f"El número es menor. Intentos: {intentos}")
    else:
        resultado.config(text=f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        boton_adivinar.config(state="disabled")

def reiniciar_juego():
    global numero_objetivo, intentos
    numero_objetivo = random.randint(1, 100)
    intentos = 0
    resultado.config(text="Adivina el número entre 1 y 100.")
    boton_adivinar.config(state="normal")
    entry.delete(0, tk.END)

# Configuración de la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Juego Adivinar el Número")

# Etiquetas, entrada y botón
instrucciones = tk.Label(ventana, text="Adivina el número entre 1 y 100:")
instrucciones.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_adivinar = tk.Button(ventana, text="Adivinar", command=adivinar_numero)
boton_adivinar.pack()

resultado = tk.Label(ventana, text="Adivina el número entre 1 y 100.")
resultado.pack()

boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.pack()

# Inicialización del juego
numero_objetivo = random.randint(1, 100)
intentos = 0

# Ejecutar la interfaz
ventana.mainloop()
