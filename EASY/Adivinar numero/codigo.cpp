#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void adivinar_numero() {
    int numero_objetivo = rand() % 100 + 1;  // Número aleatorio entre 1 y 100
    int adivinanza, intentos = 0, max_intentos = 10;

    cout << "Adivina el número entre 1 y 100. Tienes " << max_intentos << " intentos." << endl;

    while (intentos < max_intentos) {
        intentos++;
        cout << "Intento #" << intentos << ": Ingresa tu adivinanza: ";
        cin >> adivinanza;

        if (adivinanza < numero_objetivo) {
            cout << "El número es mayor." << endl;
        } else if (adivinanza > numero_objetivo) {
            cout << "El número es menor." << endl;
        } else {
            cout << "¡Felicidades! Has adivinado el número en " << intentos << " intentos." << endl;
            return;
        }
    }

    cout << "Lo siento, has agotado tus intentos. El número era " << numero_objetivo << "." << endl;
}

int main() {
    srand(time(0));  // Inicializar la semilla del generador de números aleatorios
    adivinar_numero();
    return 0;
}
