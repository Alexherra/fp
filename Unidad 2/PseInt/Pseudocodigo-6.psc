Algoritmo NumeroMayorDeTres
	Definir Numero1 Como Entero
	Definir Numero2 Como Entero
	Definir Numero3 Como Entero
	
	Escribir "Ingrese los numeros"
	Leer Numero1
	Leer Numero2
	Leer Numero3
	
	si Numero1>Numero2 o Numero1>Numero3 Entonces
		Escribir Numero1
	SiNo
		Si Numero2>Numero1 O Numero2>Numero3 Entonces
			Escribir Numero2
		SiNo
			Si	Numero3>Numero1 o Numero3>Numero2 Entonces
				Escribir Numero3
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo	