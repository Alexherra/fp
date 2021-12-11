Algoritmo NombreCompletoDeDosPersonas
	Definir nombre1 Como Caracter
	Definir nombre2 Como Caracter
	
	Escribir "***Programa que cuenta numero de letras de un nombre e imprime el mayor"
	Escribir "Ingrese el primer nombre"
	Leer nombre1
	Escribir "Ingrese el segundo nombre"
	Leer nombre2
	
	N1 = Longitud(nombre1)
	N2 = Longitud(nombre2)
	Escribir "El numero de letras de primer nombre es: ",N1
	Escribir "El numero de letras del segundo nombre es: ",N2
	
	si N1>N2 Entonces
		Escribir "El nombre con mas letras es: ", nombre1 
		Sino Escribir "El nombre don mas letras es: ", nombre2
		FinSi
FinAlgoritmo
