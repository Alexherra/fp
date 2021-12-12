#Programa que realize un sorteo con numeros del 1 al 10

print("")
print("Programa que realize sorteo")
print("")
print("El numero debe de ser del 1 al 10")

print("Ingrese el numero con el que desea participar")
numero=(input("Ingreselo aqui "))
print("")

numero1=numero
import random

sorteo1=random.randint(1,10)

if numero==sorteo1:
	print("Eres el ganador con el numero ",sorteo1)

else:
	print("Sigue partipano el numero ",numero,"no fue el ganador")

print("")
print("El Programa a finalizado")