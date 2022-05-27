#Matias Tapia
#ejercicio 1

def calculo_letras_por_palabra(palabra, letra):
  #se inicializa una suma en 0 para contar la letra repetida
  suma = 0
  
  #luego se hace la funcion upper para que cada letra este en mayuscula y se puede contar correctamente si la letra se repite
  palabra = palabra.upper()
  letra = letra.upper()
  #el ciclo for recorre la palabra una por una, con el if se compara la letra con la x
  for x in palabra:
    #print(x)
    if( letra == x):
      suma += 1
  return suma

#inicio de variables input
palabra = input("Ingrese palabra: ")
letra = input("Ingrese letra: ")

#uso funcion
suma = calculo_letras_por_palabra(palabra, letra)
suma = str(suma)
palabra = str(palabra)
letra = str(letra)
print("La letra '" + letra + "' en la palabra '" +palabra + "' se repte " + suma + " vez/veces")
