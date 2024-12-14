#include <iostream>
using namespace std;

void calculadora() {
    int opcion;
    double num1, num2;

    cout << "Bienvenido a la calculadora" << endl;
    cout << "Opciones:" << endl;
    cout << "1. Suma" << endl;
    cout << "2. Resta" << endl;
    cout << "3. Multiplicación" << endl;
    cout << "4. División" << endl;
    cout << "5. Salir" << endl;

    while (true) {
        cout << "\nSelecciona una opción (1-5): ";
        cin >> opcion;

        if (opcion == 5) {
            cout << "Saliendo de la calculadora. ¡Hasta luego!" << endl;
            break;
        }

        if (opcion < 1 || opcion > 4) {
            cout << "Por favor, selecciona una opción válida." << endl;
            continue;
        }

        cout << "Ingresa el primer número: ";
        cin >> num1;
        cout << "Ingresa el segundo número: ";
        cin >> num2;

        switch (opcion) {
            case 1:
                cout << "Resultado: " << num1 << " + " << num2 << " = " << num1 + num2 << endl;
                break;
            case 2:
                cout << "Resultado: " << num1 << " - " << num2 << " = " << num1 - num2 << endl;
                break;
            case 3:
                cout << "Resultado: " << num1 << " * " << num2 << " = " << num1 * num2 << endl;
                break;
            case 4:
                if (num2 == 0) {
                    cout << "Error: No se puede dividir entre cero." << endl;
                } else {
                    cout << "Resultado: " << num1 << " / " << num2 << " = " << num1 / num2 << endl;
                }
                break;
            default:
                cout << "Opción no válida." << endl;
                break;
        }
    }
}

int main() {
    calculadora();
    return 0;
}
