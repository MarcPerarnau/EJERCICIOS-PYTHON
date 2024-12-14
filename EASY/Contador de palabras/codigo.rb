# Contador de palabras en Ruby

def contar_palabras(texto)
    palabras = texto.split(/\W+/).reject { |palabra| palabra.empty? }
    total_palabras = palabras.length
    total_caracteres = texto.length
    palabras_unicas = palabras.uniq.length
  
    puts "Número total de palabras: #{total_palabras}"
    puts "Número total de caracteres: #{total_caracteres}"
    puts "Número de palabras únicas: #{palabras_unicas}"
  end
  
  puts "Introduce el texto para contar las palabras:"
  texto = gets.chomp
  contar_palabras(texto)
  