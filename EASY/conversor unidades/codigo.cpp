#include <iostream>
#include <string>
#include <map>
using namespace std;

double convertir_longitud(double valor, string de, string a) {
    map<string, double> conversiones = {
        {"metros", 1.0},
        {"kilometros", 1000.0},
        {"millas", 1609.34},
        {"yardas", 0.9144}
    };
    return valor * conversiones[a] / conversiones[de];
}

double convertir_masa(double valor, string de, string a) {
    map<string, double> conversiones = {
        {"gramos", 1.0},
        {"kilogramos", 1000.0},
        {"libras", 453.592},
        {"onzas", 28.3495}
    };
    return valor * conversiones[a] / conversiones[de];
}

double convertir_temperatura(double valor, string de, string a) {
    if (de == "Celsius" && a == "Fahrenheit")
        return valor * 9 / 5 + 32;
    if (de == "Fahrenheit" && a == "Celsius")
        return (valor - 32) * 5 / 9;
    if (de == "Celsius" && a == "Kelvin")
        return valor + 273.15;
    if (de == "Kelvin" && a == "Celsius")
        return valor - 273.15;
    if (de == "Fahrenheit" && a == "Kelvin")
        return (valor - 32) * 5 / 9 + 273.15;
    if (de == "Kelvin" && a == "Fahrenheit")
        return (valor - 273.15) * 9 / 5 + 32;
    return valor;
}

void conversor() {
    cout << "Bienvenido al Conversor de Unidades" << endl;
    cout << "Seleccione la categoria: 1. Longitud 2. Masa 3. Temperatura" << endl;
    int categoria;
    cin >> categoria;

    cout << "Ingresa el valor a convertir: ";
    double valor;
    cin >> valor;

    string de, a;
    switch (categoria) {
        case 1:
            cout << "Seleccione las unidades de Longitud: metros, kilometros, millas, yardas" << endl;
            cout << "De: ";
            cin >> de;
            cout << "A: ";
            cin >> a;
            cout << "Resultado: " << convertir_longitud(valor, de, a) << " " << a << endl;
            break;
        case 2:
            cout << "Seleccione las unidades de Masa: gramos, kilogramos, libras, onzas" << endl;
            cout << "De: ";
            cin >> de;
            cout << "A: ";
            cin >> a;
            cout << "Resultado: " << convertir_masa(valor, de, a) << " " << a << endl;
            break;
        case 3:
            cout << "Seleccione las unidades de Temperatura: Celsius, Fahrenheit, Kelvin" << endl;
            cout << "De: ";
            cin >> de;
            cout << "A: ";
            cin >> a;
            cout << "Resultado: " << convertir_temperatura(valor, de, a) << " " << a << endl;
            break;
        default:
            cout << "Opción no válida" << endl;
    }
}

int main() {
    conversor();
    return 0;
}
