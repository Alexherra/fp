#Programa para sacer el area de figuras(Circulo, Cuadrado, Rectangulo y Triangulo)

print("Sacar el area de figuras (Circulo, Cuadrado, Rectangulo y Triangulo)")
print("")
print("Para sacar el area de la figura deseada, ")
print("tendra que usar los numeros que se muestran enseguida")
print("")

opcion=True

while opcion>0 or opcion<=5:
	print("1 Para elegir el area de un circulo")
	print("2 Para elegir el area de un cuadrado")
	print("3 Para elegir el area de un rectangulo")
	print("4 Para elegir el area de un triangulo")
	print("5 Para Finalizar")
	print(" ")

	print("Ingrese aqui el el numero de la figura a la que desea sacar el area")
	opcion=float(input("Ingreselo aqui "))
	
	
	if opcion==1:
		print(" ")
		print("Ingrese el radio del circulo")
		radio=float(input("Ingreselo aqui "))
		print(" ")

		total1= (radio*radio*3.1416)

		print("El area del circulo es = ", total1)
		print(" ")

	elif opcion==2:
		print(" ")
		print("Ingrese el lado del cuadrado")
		lado=float(input("Ingreselo aqui "))
		print(" ")

		total2= (lado*lado)

		print("El area del cuadrado es = ", total2)
		print(" ")
	
	elif opcion==3:
		print("")
		print("Ingrese el tamaño de la base")
		base=float(input("Ingreselo aqui "))
		print("Ahora ingrese el tamaño de la altura")
		altura1=float(input("Ingreselo aqui "))

		total3= (base*altura1)

		print("El area del rectangulo es = ", total3)
		print(" ")

	elif opcion==4:
		print(" ")
		print("Ingrese el tamaño de la altura")
		altura2=float(input("Ingreselo aqui "))
		print("Ahara ingrese el tamaño de la base")
		base2=float(input("Ingreselo aqui "))

		triangulo= (altura2*base2)
		total4= (triangulo/2)

		print("El area del triangulo es = ", total4)
		print("")

	elif opcion==5:
		print("")
		print("El programa a finalizado")	
		break;

print("**Gracias**")