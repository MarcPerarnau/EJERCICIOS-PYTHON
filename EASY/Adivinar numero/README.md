# Juego adivinar número
Este proyecto es un juego de adivinar el número implementado en tres lenguajes de programación: Python, Ruby, C++ y Python (con Tkinter). El juego genera un número aleatorio dentro de un rango determinado y el jugador debe adivinarlo mediante pistas proporcionadas después de cada intento.

## Características

- El programa genera un número aleatorio en un rango determinado.
- El jugador debe adivinar el número ingresando intentos y recibir pistas (mayor o menor).
- El juego continúa hasta que el jugador adivina el número o se queda sin intentos.
- Las versiones en **Python** utilizan una interfaz gráfica con **Tkinter**.
- Las versiones en **Ruby** y **C++** son aplicaciones de consola.

## Instrucciones de uso

### Ruby
Instala Ruby si aún no lo tienes instalado: [Instalar Ruby](https://www.ruby-lang.org/es/documentation/installation/).
2. Guarda el archivo de Ruby como `adivinar_numero.rb`.
3. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
   ```bash
   ruby adivinar_numero.rb
   ```
4. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
5. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### C++
1. Instala un compilador de C++ como g++ si aún no lo tienes instalado: Instalar g++.
2. Guarda el archivo de C++ como ``adivinar_numero.cpp``.
3. Abre una terminal, navega al directorio donde guardaste el archivo y compílalo con el siguiente comando:
```bash
g++ adivinar_numero.cpp -o adivinar_numero
```
4. Ejecuta el programa con:
```bash
./adivinar_numero
```
5. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
6. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### Python (con Tkinter)
1. Instala Python si aún no lo tienes: Instalar Python.
2. Tkinter debería estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo con:
```bash
pip install tk
```
3. Guarda el archivo Python como adivinar_numero.py.
4. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
```bash
python adivinar_numero.py
```
5. La aplicación se abrirá en una ventana gráfica donde podrás seleccionar las unidades de origen y destino, ingresar el valor a convertir y ver el resultado.
## Requisitos
- Ruby (para la versión Ruby)
- g++ (para la versión C++)
- Python con Tkinter (para la versión Python)
## Notas
- En la versión Python con Tkinter, el juego se presenta con una interfaz gráfica que facilita la interacción.
- Las versiones en Ruby y C++ funcionan como aplicaciones de consola y son ideales para entornos de terminal.
- El número generado aleatoriamente siempre estará dentro del rango establecido (por ejemplo, entre 1 y 100).
- Si te quedas sin intentos antes de adivinar el número, el juego termina y se muestra el número correcto.
## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.