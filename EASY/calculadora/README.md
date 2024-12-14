# Calculadora Básica

Este proyecto incluye una calculadora básica implementada en tres lenguajes de programación: Ruby, C++ y Python (con Tkinter para la interfaz gráfica). La calculadora permite realizar operaciones de suma, resta, multiplicación y división.

## Características

- **Operaciones soportadas**:
  - Suma
  - Resta
  - Multiplicación
  - División
- La calculadora permite al usuario ingresar dos números y realizar una operación matemática seleccionada.
- En Python, se utiliza **Tkinter** para crear una interfaz gráfica de usuario (GUI).

## Instrucciones de uso

### Ruby

1. Instala Ruby si aún no lo tienes instalado: [Instalar Ruby](https://www.ruby-lang.org/es/documentation/installation/).
2. Guarda el archivo de Ruby como `calculadora.rb`.
3. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
   ```bash
   ruby calculadora.rb

### C++
1. Instala un compilador de C++ como g++ si aún no lo tienes instalado: Instalar g++.
2. Guarda el archivo de C++ como calculadora.cpp.
3. Abre una terminal, navega al directorio donde guardaste el archivo y compílalo con el siguiente comando:
```bash
g++ calculadora.cpp -o calculadora
```
4. Ejecuta el programa con:
```bash
./calculadora
```
5. Sigue las instrucciones en la terminal para seleccionar una operación y proporcionar los números.

### Python (con Tkinter)
1. Instala Python si aún no lo tienes: Instalar Python.
2. Tkinter debería estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo con:
```bash
pip install tk
```
3. Guarda el archivo Python como calculadora.py.
4. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
```bash
python calculadora.py
```
5. La aplicación se abrirá en una ventana gráfica donde podrás ingresar los números y realizar las operaciones.

### Requisitos
- Ruby (para la versión Ruby)
- g++ (para la versión C++)
- Python con Tkinter (para la versión Python)
## Notas
- En la versión Python, la interfaz gráfica facilita la interacción con el programa, mientras que las versiones Ruby y C++ son aplicaciones de consola.
- En todas las versiones, se gestiona la división por cero, mostrando un mensaje de error en caso de intentar dividir por cero.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.