# Conversor de Unidades

Este proyecto es un **conversor de unidades** básico implementado en tres lenguajes de programación:**Pythob**, **Ruby**, **C++** y **Python (con Tkinter)**. El conversor permite convertir entre varias unidades de medida comunes, como longitud, masa y temperatura.

## Características

- **Unidades soportadas**:
  - **Longitud**: metros, kilómetros, millas, yardas, etc.
  - **Masa**: gramos, kilogramos, libras, onzas, etc.
  - **Temperatura**: Celsius, Fahrenheit, Kelvin.
  
- El programa permite al usuario seleccionar una unidad de origen y una de destino, e ingresar el valor a convertir.
- En la versión Python, se utiliza **Tkinter** para crear una interfaz gráfica de usuario (GUI).

## Instrucciones de uso

### Ruby

1. Instala Ruby si aún no lo tienes instalado: [Instalar Ruby](https://www.ruby-lang.org/es/documentation/installation/).
2. Guarda el archivo de Ruby como `conversor.rb`.
3. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
   ```bash
   ruby conversor.rb
   ```
4. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
5. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### C++
1. Instala un compilador de C++ como g++ si aún no lo tienes instalado: Instalar g++.
2. Guarda el archivo de C++ como ``conversor.cpp``.
3. Abre una terminal, navega al directorio donde guardaste el archivo y compílalo con el siguiente comando:
```bash
g++ conversor.cpp -o conversor
```
4. Ejecuta el programa con:
```bash
./conversor
```
5. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
6. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### Python (con Tkinter)
1. Instala Python si aún no lo tienes: Instalar Python.
2. Tkinter debería estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo con:
```bash
pip install tk
```
3. Guarda el archivo Python como conversor.py.
4. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
```bash
python conversor.py
```
5. La aplicación se abrirá en una ventana gráfica donde podrás seleccionar las unidades de origen y destino, ingresar el valor a convertir y ver el resultado.
## Requisitos
- Ruby (para la versión Ruby)
- g++ (para la versión C++)
- Python con Tkinter (para la versión Python)
## Notas
- En la versión Python, la interfaz gráfica facilita la interacción con el programa, mientras que las versiones Ruby y C++ son aplicaciones de consola.
- El conversor permite realizar conversiones precisas entre diferentes unidades, con una amplia variedad de opciones para longitud, masa y temperatura.
## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.