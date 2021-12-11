#Programa que imprime el nombre y de dos personas e imprime el numero de letras


n1=input("Ingrese el primer nombre")
n2=input("Ingrese el segundo nombre")

n3=len(n1)
n4=len(n2)

print("El numero de letras del primer nombre es:",(n3))
print("El numero de letras del segundo nombre es",(n4))

if n3>n4:
	print("El nombre con mas letras es:",(n1))
elif n3<n4:
	print("El nombre con mas letras es:",(n2))

print ("Finalizado")