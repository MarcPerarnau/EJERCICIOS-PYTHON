# Juego de adivinar el número en Ruby

def adivinar_numero
    numero_objetivo = rand(1..100)  # Número aleatorio entre 1 y 100
    intentos = 0
    max_intentos = 10
    
    puts "Adivina el número entre 1 y 100. Tienes #{max_intentos} intentos."
    
    while intentos < max_intentos
      intentos += 1
      print "Intento ##{intentos}: Ingresa tu adivinanza: "
      adivinanza = gets.chomp.to_i
      
      if adivinanza < numero_objetivo
        puts "El número es mayor."
      elsif adivinanza > numero_objetivo
        puts "El número es menor."
      else
        puts "¡Felicidades! Has adivinado el número en #{intentos} intentos."
        return
      end
    end
    
    puts "Lo siento, has agotado tus intentos. El número era #{numero_objetivo}."
  end
  
  adivinar_numero
  