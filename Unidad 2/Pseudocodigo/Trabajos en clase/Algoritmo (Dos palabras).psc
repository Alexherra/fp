Algoritmo Dos_palabras
	Definir palabra1, palabra2  Como Caracter
	
	Escribir "Ingresa primera palabra"
	leer palabra1
	palabra1 <- Mayusculas(palabra1)
	Escribir "Ingresa segunda palabra"
	leer palabra2
	palabra2 <- Mayusculas(palabra2)
	Si Longitud(palabra1) < Longitud(palabra2) Entonces
		Escribir palabra2
	SiNo
		Escribir palabra1
	FinSi
FinAlgoritmo
