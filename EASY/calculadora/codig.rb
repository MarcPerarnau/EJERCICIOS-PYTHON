def calculadora
    puts "Bienvenido a la calculadora"
    puts "Opciones:"
    puts "1. Suma"
    puts "2. Resta"
    puts "3. Multiplicación"
    puts "4. División"
    puts "5. Salir"
  
    while true
      print "\nSelecciona una opción (1-5): "
      opcion = gets.chomp.to_i
  
      if opcion == 5
        puts "Saliendo de la calculadora. ¡Hasta luego!"
        break
      end
  
      if opcion < 1 || opcion > 4
        puts "Por favor, selecciona una opción válida."
        next
      end
  
      print "Ingresa el primer número: "
      num1 = gets.chomp.to_f
      print "Ingresa el segundo número: "
      num2 = gets.chomp.to_f
  
      case opcion
      when 1
        puts "Resultado: #{num1} + #{num2} = #{num1 + num2}"
      when 2
        puts "Resultado: #{num1} - #{num2} = #{num1 - num2}"
      when 3
        puts "Resultado: #{num1} * #{num2} = #{num1 * num2}"
      when 4
        if num2 == 0
          puts "Error: No se puede dividir entre cero."
        else
          puts "Resultado: #{num1} / #{num2} = #{num1 / num2}"
        end
      end
    end
  end
  
  calculadora
  