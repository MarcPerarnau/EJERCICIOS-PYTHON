# Contador de palabras

Este proyecto es un **contador de palabras** implementado en tres lenguajes de programación: **Python**, **Ruby**, **C++** y **Python (con Tkinter)**. El programa cuenta la cantidad de palabras en un texto ingresado por el usuario. Además, proporciona estadísticas adicionales, como el número de caracteres y la cantidad de palabras únicas.

## Características

- El programa cuenta el número total de palabras en un texto.
- Muestra el número total de caracteres en el texto.
- Proporciona el número de palabras únicas (sin repetir).
- La versión **Python con Tkinter** incluye una interfaz gráfica para facilitar la interacción.
- Las versiones en **Ruby** y **C++** son aplicaciones de consola.

## Instrucciones de uso

### Ruby

1. Instala Ruby si aún no lo tienes instalado: [Instalar Ruby](https://www.ruby-lang.org/es/documentation/installation/).
2. Guarda el archivo de Ruby como `contador_palabras.rb`.
3. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
   ```bash
   ruby contador_palabras.rb
   ```
4. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
5. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### C++
1. Instala un compilador de C++ como g++ si aún no lo tienes instalado: Instalar g++.
2. Guarda el archivo de C++ como ``contador_palabras.cpp``.
3. Abre una terminal, navega al directorio donde guardaste el archivo y compílalo con el siguiente comando:
```bash
g++ contador_palabras.cpp -o contador_palabras
```
4. Ejecuta el programa con:
```bash
./contador_palabras
```
5. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
6. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### Python (con Tkinter)
1. Instala Python si aún no lo tienes: Instalar Python.
2. Tkinter debería estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo con:
```bash
pip install tk
```
3. Guarda el archivo Python como contador_palabras.py.
4. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
```bash
python contador_palabras.py
```
5. La aplicación se abrirá en una ventana gráfica donde podrás seleccionar las unidades de origen y destino, ingresar el valor a convertir y ver el resultado.
## Requisitos
- Ruby (para la versión Ruby)
- g++ (para la versión C++)
- Python con Tkinter (para la versión Python)
## Notas
- En la versión **Python con Tkinter**, la interfaz gráfica facilita la interacción, permitiendo ingresar texto y ver los resultados de manera visual.
- Las versiones en **Ruby** y **C++** son aplicaciones de consola, ideales para entornos de terminal.
- El contador considera palabras separadas por espacios y elimina signos de puntuación para contar las palabras correctamente.
## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.