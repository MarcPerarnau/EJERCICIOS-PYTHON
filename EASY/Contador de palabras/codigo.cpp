#include <iostream>
#include <sstream>
#include <set>
#include <string>
#include <cctype>

using namespace std;

void contar_palabras(const string& texto) {
    int total_palabras = 0, total_caracteres = texto.length();
    set<string> palabras_unicas;
    stringstream ss(texto);
    string palabra;

    while (ss >> palabra) {
        // Eliminar signos de puntuación al principio y al final de la palabra
        palabra.erase(0, palabra.find_first_not_of(" \t\r\n"));
        palabra.erase(palabra.find_last_not_of(" \t\r\n") + 1);
        
        // Agregar la palabra al set de palabras únicas
        palabras_unicas.insert(palabra);
        total_palabras++;
    }

    cout << "Número total de palabras: " << total_palabras << endl;
    cout << "Número total de caracteres: " << total_caracteres << endl;
    cout << "Número de palabras únicas: " << palabras_unicas.size() << endl;
}

int main() {
    string texto;
    cout << "Introduce el texto para contar las palabras: ";
    getline(cin, texto);

    contar_palabras(texto);

    return 0;
}
