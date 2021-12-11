Algoritmo ClaseYAtributos
	Definir nombre Como Caracter
	Definir atributo Como Caracter
	Definir atributo1 Como Caracter
	Definir atributo2 Como Caracter
	Definir arreglo Como Caracter
	
	Escribir "--Programa que pide nombre de clase y los atributos de la misma--"
	Escribir "Nombre de la clase"
	Leer nombre
	Escribir "Ingrese primer atributo"
	Leer atributo
	Escribir "Ingrese segundo atributo"
	Leer atributo1
	Escribir "Ingrese tercer atributo"
	Leer atributo2
	
	Dimension arreglo[3]
	arreglo[1] = atributo
	arreglo[2] = atributo1 
	arreglo[3] = atributo2
	
	Imprimir "El nombre de la clase es: " ,nombre
	Imprimir "Los atributos son ",arreglo[1]," " ,arreglo[2]," ",arreglo[3]
	
FinAlgoritmo
