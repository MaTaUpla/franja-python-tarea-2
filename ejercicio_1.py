def calculo_letras_por_palabra(palabra, letra):
  #Se inicializa una suma en 0 para contar la letra repetida
  suma = 0
  #Luego se hace la funcion upper para que cada letra este en mayuscula y se puede contar correctamente si la letra se repite
  palabra = palabra.upper()
  letra = letra.upper()
  #El ciclo for recorre la palabra una por una, con el if se compara la letra con la x
  for x in palabra:
    if( letra == x):
      suma += 1

  if(suma == 1):
    suma = str(suma)
    print("La letra '" + letra + "' en la palabra '" + palabra + "' se repite " + suma + " vez")
  elif(suma == 0):
    suma = str(suma)
    print("La letra '" + letra + "' en la palabra '" + palabra + "' nose se repite ninguna vez")
  else:
    suma = str(suma)
    print("La letra '" + letra + "' en la palabra '" + palabra + "' se repite " + suma + " veces")

#Función principal
def main():
  #Inicio de variables input
  print("############################################")
  print("Contador de letras repetidas en una palabra")
  print("############################################")
  palabra = input("Ingrese palabra: ")
  letra = input("Ingrese letra: ")

  #Uso funcion
  calculo_letras_por_palabra(palabra, letra)

#Punto de entrada
if __name__ == "__main__":
    main()
