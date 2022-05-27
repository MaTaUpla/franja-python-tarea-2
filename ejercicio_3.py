#Matias Tapia
#ejercicio 3

def calculo_valor_entrada(edad):
  precio = 0
  if(edad < 4):
    precio = 0
  elif(edad >= 4 and edad <= 18):
    precio = 3500
  else:
    precio = 8000
  return str(precio)

edad = input("ingrese su edad para comprar la entrada: ")
precio = calculo_valor_entrada(int(edad))

print("")
if(int(precio) == 0):
 print("Su entrada es gratis ya que la edad del cliente es " + edad + " año(s)")
else:
  print("Su entrada tiene un valor de $" + precio + " ya que la edad del cliente es " + edad + " años")
