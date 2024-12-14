# Generador de contraseñas en Ruby

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    caracteres = ('a'..'z').to_a
    caracteres += ('A'..'Z').to_a if incluir_mayusculas
    caracteres += ('0'..'9').to_a if incluir_numeros
    caracteres += ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?'] if incluir_simbolos
  
    contrasena = ''
    longitud.times { contrasena += caracteres.sample }
    contrasena
  end
  
  puts "Generador de contraseñas"
  print "Ingresa la longitud de la contraseña: "
  longitud = gets.chomp.to_i
  
  print "¿Incluir mayúsculas? (s/n): "
  incluir_mayusculas = gets.chomp.downcase == 's'
  
  print "¿Incluir números? (s/n): "
  incluir_numeros = gets.chomp.downcase == 's'
  
  print "¿Incluir símbolos? (s/n): "
  incluir_simbolos = gets.chomp.downcase == 's'
  
  contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
  puts "Contraseña generada: #{contrasena}"
  