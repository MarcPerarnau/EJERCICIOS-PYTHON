# Agenda de Contactos
Este proyecto es una agenda de contactos que permite a los usuarios almacenar, buscar, actualizar y eliminar contactos. Los datos se guardan en un archivo de formato CSV o JSON, lo que facilita su manejo y portabilidad. El programa está implementado en tres lenguajes de programación: **Python**, **Ruby**, **C++** , y también tiene una versión en **Python con Tkinter** con una interfaz gráfica.

## Características

- Guardar contactos con información como nombre, número de teléfono y correo electrónico.
- Buscar contactos por nombre, número o correo.
- Eliminar contactos fácilmente.
- Actualizar información de un contacto existente.
- Soporte para archivos en formato CSV o JSON.
- Interfaz gráfica en la versión Python con Tkinter.
- Aplicaciones de consola en Ruby, C++, y Python.

## Instrucciones de uso

### Ruby
Instala Ruby si aún no lo tienes instalado: [Instalar Ruby](https://www.ruby-lang.org/es/documentation/installation/).
2. Guarda el archivo de Ruby como `agenda_contactos.rb`.
3. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
   ```bash
   ruby agenda_contactos.rb
   ```
 4. Usa el menú para:
  4.1 Agregar un contacto.
  4.2 Buscar un contacto.
  4.3 Actualizar información de un contacto.
  4.4 Eliminar un contacto.
  5.5 Mostrar todos los contactos.
5. Los datos se guardarán automáticamente en un archivo CSV o JSON (dependiendo de tu elección).
### C++
1. Instala un compilador de C++ como g++ si aún no lo tienes instalado: Instalar g++.
2. Guarda el archivo de C++ como ``agenda_contactos.cpp``.
3. Abre una terminal, navega al directorio donde guardaste el archivo y compílalo con el siguiente comando:
```bash
g++ agenda_contactos.cpp -o agenda_contactos
```
4. Ejecuta el programa con:
```bash
./agenda_contactos
```
5. ESigue las instrucciones para agregar, buscar, actualizar o eliminar contactos.
6. Los datos se almacenarán en un archivo CSV o JSON, según lo configurado.
### Python (con Tkinter)
1. Instala Python si aún no lo tienes: Instalar Python.
2. Tkinter debería estar instalado por defecto con Python. Si no lo tienes, puedes instalarlo con:
```bash
pip install tk
```
3. Guarda el archivo Python como agenda_contactos.py.
4. Abre una terminal, navega al directorio donde guardaste el archivo y ejecuta el siguiente comando:
```bash
python agenda_contactos.py
```
5. Se abrirá una ventana gráfica donde podrás agregar, buscar, actualizar y eliminar contactos de forma visual.
## Requisitos
- Ruby (para la versión Ruby)
- g++ (para la versión C++)
- Python con Tkinter (para la versión Python)
- Archivos CSV o JSON como formato de almacenamiento.
## Notas
- La versión en Python con Tkinter es más amigable para los usuarios no técnicos, ya que ofrece una interfaz gráfica.
- En las versiones de consola, los contactos se manipulan mediante menús interactivos en la terminal.
- El programa garantiza la persistencia de los datos al almacenarlos en archivos CSV o JSON, que pueden ser fácilmente importados o exportados.
## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.