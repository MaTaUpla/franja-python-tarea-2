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
  edad = str(edad)
  if(precio == 0):
    if(int(edad) == 1):
      print("La entrada es gratis ya que la edad del cliente es de " + edad + " año")
    else:
      print("La entrada es gratis ya que la edad del cliente es de " + edad + " años")
  else:
    print("La entrada tiene un valor de $" + str(precio) + " ya que la edad del cliente es de " + edad + " años")

#Función principal
def main():
  print("####################")
  print("Comprar de entradas")
  edad = int(input("Ingrese su edad: "))
  print("####################")
  calculo_valor_entrada(edad)

#Punto de entrada
if __name__ == "__main__":
    main()
