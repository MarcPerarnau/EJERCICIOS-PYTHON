def convertir_longitud(valor, de, a)
    conversiones = {
      "metros" => 1.0,
      "kilometros" => 1000.0,
      "millas" => 1609.34,
      "yardas" => 0.9144
    }
    valor * conversiones[a] / conversiones[de]
  end
  
  def convertir_masa(valor, de, a)
    conversiones = {
      "gramos" => 1.0,
      "kilogramos" => 1000.0,
      "libras" => 453.592,
      "onzas" => 28.3495
    }
    valor * conversiones[a] / conversiones[de]
  end
  
  def convertir_temperatura(valor, de, a)
    if de == "Celsius" && a == "Fahrenheit"
      valor * 9 / 5 + 32
    elsif de == "Fahrenheit" && a == "Celsius"
      (valor - 32) * 5 / 9
    elsif de == "Celsius" && a == "Kelvin"
      valor + 273.15
    elsif de == "Kelvin" && a == "Celsius"
      valor - 273.15
    elsif de == "Fahrenheit" && a == "Kelvin"
      (valor - 32) * 5 / 9 + 273.15
    elsif de == "Kelvin" && a == "Fahrenheit"
      (valor - 273.15) * 9 / 5 + 32
    else
      valor
    end
  end
  
  def conversor
    puts "Bienvenido al Conversor de Unidades"
    puts "Seleccione la categoría: 1. Longitud 2. Masa 3. Temperatura"
    categoria = gets.chomp.to_i
  
    puts "Ingresa el valor a convertir: "
    valor = gets.chomp.to_f
  
    case categoria
    when 1
      puts "Seleccione las unidades de Longitud: metros, kilometros, millas, yardas"
      puts "De: "
      de = gets.chomp.downcase
      puts "A: "
      a = gets.chomp.downcase
      puts "Resultado: #{convertir_longitud(valor, de, a)} #{a}"
    when 2
      puts "Seleccione las unidades de Masa: gramos, kilogramos, libras, onzas"
      puts "De: "
      de = gets.chomp.downcase
      puts "A: "
      a = gets.chomp.downcase
      puts "Resultado: #{convertir_masa(valor, de, a)} #{a}"
    when 3
      puts "Seleccione las unidades de Temperatura: Celsius, Fahrenheit, Kelvin"
      puts "De: "
      de = gets.chomp
      puts "A: "
      a = gets.chomp
      puts "Resultado: #{convertir_temperatura(valor, de, a)} #{a}"
    else
      puts "Opción no válida"
    end
  end
  
  conversor
  