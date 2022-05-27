#Matias Tapia
#ejercicio 2

#formula del area de un circulo Area = pi * Radio^2
def calculo_area_circulo(radio):
  pi = 3.14
  area = (pi * pow(radio,2))
  return round(area,1)

#formula del volumen del cilindro Volumen = Area * altura 
#uso la funcion del area en el volumen
def calculo_volumen_cilindro(radio, altura):
  area = calculo_area_circulo(radio)
  volumen = area * altura
  return round(volumen,1)

#input de radio y altura
radio_circulo = input("Ingrese valor del radio del circulo: ")
radio_cilindro = input("Ingrese valor de la altura del cilindro: ")
altura_cilindro = input("Ingrese valor de la altura del cilindro: ")

print("")
#uso funciones para calculos
area = calculo_area_circulo(int(radio_circulo))
volumen = calculo_volumen_cilindro(int(radio_cilindro), int(altura_cilindro))

print("el area del circulo de radio " + radio_circulo + " cm, es de " + str(area) + " cm2")
print("el volumen del cilindro de radio " + radio_cilindro + " cm y altura " + altura_cilindro + " cm, es de " + str(volumen) + " cm3")