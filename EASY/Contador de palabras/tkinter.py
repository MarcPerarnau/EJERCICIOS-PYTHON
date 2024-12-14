import tkinter as tk

def contar_palabras():
    texto = entry_text.get("1.0", tk.END)
    palabras = texto.split()
    total_palabras = len(palabras)
    total_caracteres = len(texto.strip())
    palabras_unicas = len(set(palabras))

    resultado_label.config(text=f"Número total de palabras: {total_palabras}\n"
                               f"Número total de caracteres: {total_caracteres}\n"
                               f"Número de palabras únicas: {palabras_unicas}")

# Configuración de la ventana de Tkinter
ventana = tk.Tk()
ventana.title("Contador de Palabras")

# Etiqueta y cuadro de texto
entrada_label = tk.Label(ventana, text="Introduce el texto:")
entrada_label.pack()
entry_text = tk.Text(ventana, height=10, width=50)
entry_text.pack()

# Botón para contar palabras
boton_contar = tk.Button(ventana, text="Contar Palabras", command=contar_palabras)
boton_contar.pack()

# Etiqueta para mostrar los resultados
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Ejecutar la interfaz
ventana.mainloop()
