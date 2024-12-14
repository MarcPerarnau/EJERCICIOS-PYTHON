# Contador de palabras en Python

def contar_palabras(texto):
    palabras = texto.split()
    total_palabras = len(palabras)
    total_caracteres = len(texto)
    palabras_unicas = len(set(palabras))

    print(f"Número total de palabras: {total_palabras}")
    print(f"Número total de caracteres: {total_caracteres}")
    print(f"Número de palabras únicas: {palabras_unicas}")

if __name__ == "__main__":
    texto = input("Introduce el texto para contar las palabras: ")
    contar_palabras(texto)
