# Generador de contraseñas

Este proyecto es un **generador de contraseñas** aleatorias implementado en tres lenguajes de programación: **Python**, **Ruby**, **C++** y **Python (con Tkinter)**. El programa permite generar contraseñas seguras con diferentes niveles de complejidad, permitiendo al usuario elegir la longitud y los caracteres que deben incluirse en la contraseña.

## Características

- Generación de contraseñas aleatorias con diferentes niveles de complejidad.
- El usuario puede elegir la longitud de la contraseña y los caracteres permitidos (mayúsculas, minúsculas, números, símbolos).
- En la versión de **Python con Tkinter**, se utiliza una interfaz gráfica para facilitar la interacción.
- Las versiones en **Ruby** y **C++** son aplicaciones de consola.

## Instrucciones de uso

### Ruby

1. Instala Ruby si aún no lo tienes instalado: [Instalar Ruby](https://www.ruby-lang.org/es/documentation/installation/).
2. Guarda el archivo de Ruby como `generador_contraseñas.rb`.
3. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
   ```bash
   ruby generador_contraseñas.rb
   ```
4. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
5. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### C++
1. Instala un compilador de C++ como g++ si aún no lo tienes instalado: Instalar g++.
2. Guarda el archivo de C++ como ``generador_contraseñas.cpp``.
3. Abre una terminal, navega al directorio donde guardaste el archivo y compílalo con el siguiente comando:
```bash
g++ generador_contraseñas.cpp -o generador_contraseñas
```
4. Ejecuta el programa con:
```bash
./generador_contraseñas
```
5. Elige la categoría de unidades que deseas convertir (longitud, masa o temperatura).
6. Ingresa el valor que deseas convertir y selecciona las unidades de origen y destino.
### Python (con Tkinter)
1. Instala Python si aún no lo tienes: Instalar Python.
2. Tkinter debería estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo con:
```bash
pip install tk
```
3. Guarda el archivo Python como generador_contraseñas.py.
4. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
```bash
python generador_contraseñas.py
```
5. La aplicación se abrirá en una ventana gráfica donde podrás seleccionar las unidades de origen y destino, ingresar el valor a convertir y ver el resultado.
## Requisitos
- Ruby (para la versión Ruby)
- g++ (para la versión C++)
- Python con Tkinter (para la versión Python)
## Notas
- En la versión Python con Tkinter, la interfaz gráfica facilita la generación de contraseñas, permitiendo seleccionar fácilmente las opciones de longitud y complejidad.
- Las versiones en Ruby y C++ funcionan como aplicaciones de consola y son ideales para entornos de terminal.
- La complejidad de la contraseña se puede ajustar eligiendo si incluir caracteres en mayúsculas, minúsculas, números o símbolos.
## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.