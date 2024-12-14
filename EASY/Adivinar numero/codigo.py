# Juego de adivinar el número en Python

import random

def adivinar_numero():
    numero_objetivo = random.randint(1, 100)  # Número aleatorio entre 1 y 100
    intentos = 0
    max_intentos = 10
    
    print(f"Adivina el número entre 1 y 100. Tienes {max_intentos} intentos.")
    
    while intentos < max_intentos:
        intentos += 1
        adivinanza = int(input(f"Intento #{intentos}: Ingresa tu adivinanza: "))
        
        if adivinanza < numero_objetivo:
            print("El número es mayor.")
        elif adivinanza > numero_objetivo:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            return
    
    print(f"Lo siento, has agotado tus intentos. El número era {numero_objetivo}.")

if __name__ == "__main__":
    adivinar_numero()
