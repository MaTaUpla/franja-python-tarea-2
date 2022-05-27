#Matias Tapia
#ejercicio 2

#inicio de variables input
palabra = input("Ingrese palabra: ")
letra = input("Ingrese letra: ")

#se inicializa una suma en 0 para contar la letra repetida
suma = 0

#el ciclo for recorre la palabra una por una, con el if se compara la letra con la x
#luego se hace la funcion upper para que cada letra este en mayuscula y se puede contar correctamente si la letra se repite
for x in palabra.upper():
  #print(x)
  if( letra.upper() == x):
    suma += 1
suma = str(suma)
palabra = str(palabra)
letra = str(letra)
print("La letra '" + letra + "' en la palabra '" +palabra + "' se repte " + suma + " vez/veces")
