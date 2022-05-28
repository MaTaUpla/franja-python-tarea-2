#Matias Tapia
#ejercicio 3

def calculo_valor_entrada(edad):
  #valor iniciado
  precio = 0
  if(edad < 4):
    precio = 0
  elif(edad >= 4 and edad <= 18):
    precio = 3500
  else:
    precio = 8000
  return str(precio)

#Función principal
def main():
  print("####################")
  print("Comprar de entradas")
  edad = input("Ingrese su edad: ")
  print("####################")
  precio = calculo_valor_entrada(int(edad))

  print("")
  if(int(precio) == 0):
    print("La entrada es gratis ya que la edad del cliente es " + edad + " año(s)")
  else:
    print("La entrada tiene un valor de $" + precio + " ya que la edad del cliente es " + edad + " años")

#Punto de entrada
if __name__ == "__main__":
    main()
