#Programa que pide nombre de un clase y pide atributos de la misma y la guarda

print("Programa que pide nombre de una clase y pide atributos")
print("")


print("Ingrese primero el nombre de la clase")
print("")

print("Ingrese el nombre de la clase")
N= input("Ingreselo aqui ")
print("")


print("Ahora ingrese los atributos de la clase")
print("")
print("Ingrese el primer atributo")
atributo1= input("Ingreselo aqui ")
print("Ingrese el segundo atributo ")
atributo2= input("Ingreselo aqui ")
print("Ingrese el tercer atributo")
atributo3= input("Ingreselo aqui ")
print("")

class nombreClase(object):
	"""docstring for nombreClase"""
	def __init__(self, A1, A2, A3):
		self.A1=A2
		self.A2=A2
		self.A3=A3

atributos= nombreClase(atributo1, atributo2, atributo3)

atributos1=[atributos.A1, atributos.A2, atributos.A3]
print("El nombre de la clase es *",N,"*")
print("Los atributos de la clase son", atributos1)
print("")

print("Gracias")