#Calculadora

print(" ")
print("**Calculadora**")
print(" ")

opcion=True
while opcion:
		print ("Para elegir la opcion requerida tendra que ingresar uno de los numeros que se muestra abajo")
		print(" ")
		print ("1 suma")
		print ("2 resta")
		print ("3 multiplicacion")
		print ("4 division")
		print ("5 para Finalizar")
		print("")

		opcion1 =float(input("Ingrese aqui la opcion a realizar"))
		numero1=float(input("Ingrese el primer valor-"))
		numero2=float(input("Ingrese el segundo valor-"))
			
		if opcion1==1:
			suma1=numero2+numero1
			print ("El resultado de la suma es =",suma1)

		elif opcion1==2:
			resta1=numero1-numero2
			print ("El resultado de la resta es =", resta1)

		elif opcion1==3:
			multiplicacion1=numero1*numero2
			print ("El resultado de la multiplicacion es =", multiplicacion1)


		elif opcion1==4:
			division1=numero1/numero2
			if numero1==0:
				print ("Inorrecto, ingrese un numero mayor a 0")
			elif numero2==0:
				print ("Inorrecto, ingrese un numero mayor a 0")
			elif numero1>0:
				print ("El resultado de la division es =", division1)
			elif numero2>0:
				print ("El resultado de la division es =", division1)
				
		elif opcion==5:
			print (" ")
			break;
			
else:
	print("El programa a Finalizado")
