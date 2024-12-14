import tkinter as tk

def realizar_operacion(opcion):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if opcion == 1:
            resultado = num1 + num2
        elif opcion == 2:
            resultado = num1 - num2
        elif opcion == 3:
            resultado = num1 * num2
        elif opcion == 4:
            if num2 == 0:
                resultado = "Error: No se puede dividir entre cero."
            else:
                resultado = num1 / num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingrese números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear entradas y etiquetas
label_num1 = tk.Label(ventana, text="Primer número:")
label_num1.pack()

entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Segundo número:")
label_num2.pack()

entry_num2 = tk.Entry(ventana)
entry_num2.pack()

# Botones para cada operación
boton_suma = tk.Button(ventana, text="Suma", command=lambda: realizar_operacion(1))
boton_suma.pack()

boton_resta = tk.Button(ventana, text="Resta", command=lambda: realizar_operacion(2))
boton_resta.pack()

boton_multiplicacion = tk.Button(ventana, text="Multiplicación", command=lambda: realizar_operacion(3))
boton_multiplicacion.pack()

boton_division = tk.Button(ventana, text="División", command=lambda: realizar_operacion(4))
boton_division.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar la aplicación
ventana.mainloop()
