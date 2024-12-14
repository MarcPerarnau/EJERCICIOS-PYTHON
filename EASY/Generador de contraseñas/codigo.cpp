#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <string>

using namespace std;

string generar_contrasena(int longitud, bool incluir_mayusculas, bool incluir_numeros, bool incluir_simbolos) {
    vector<char> caracteres;
    for (char c = 'a'; c <= 'z'; c++) caracteres.push_back(c);
    if (incluir_mayusculas) for (char c = 'A'; c <= 'Z'; c++) caracteres.push_back(c);
    if (incluir_numeros) for (char c = '0'; c <= '9'; c++) caracteres.push_back(c);
    if (incluir_simbolos) {
        string simbolos = "!@#$%^&*()-_=+[]{};:,.<>/?";
        for (char c : simbolos) caracteres.push_back(c);
    }

    string contrasena = "";
    for (int i = 0; i < longitud; i++) {
        contrasena += caracteres[rand() % caracteres.size()];
    }

    return contrasena;
}

int main() {
    srand(time(0));

    int longitud;
    cout << "Generador de contraseñas\n";
    cout << "Ingresa la longitud de la contraseña: ";
    cin >> longitud;

    char incluir_mayusculas, incluir_numeros, incluir_simbolos;
    cout << "¿Incluir mayúsculas? (s/n): ";
    cin >> incluir_mayusculas;
    cout << "¿Incluir números? (s/n): ";
    cin >> incluir_numeros;
    cout << "¿Incluir símbolos? (s/n): ";
    cin >> incluir_simbolos;

    bool incluir_mayusculas_b = (incluir_mayusculas == 's' || incluir_mayusculas == 'S');
    bool incluir_numeros_b = (incluir_numeros == 's' || incluir_numeros == 'S');
    bool incluir_simbolos_b = (incluir_simbolos == 's' || incluir_simbolos == 'S');

    string contrasena = generar_contrasena(longitud, incluir_mayusculas_b, incluir_numeros_b, incluir_simbolos_b);
    cout << "Contraseña generada: " << contrasena << endl;

    return 0;
}
