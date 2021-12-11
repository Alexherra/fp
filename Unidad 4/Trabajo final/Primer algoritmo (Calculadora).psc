Algoritmo PrimerCalculadora
	Definir numero1 Como Entero
	Definir numero2 Como Entero
	Definir signo Como Entero
	
	Escribir "***CALCULADORA***"
	Escribir "ingrese primer valor"
	Leer  numero1
	Escribir "Para realizar las operaciones deseadas tendra que ingresar un numero como estan indicados"
	Escribir "Numero 1 (Suma)"
	Escribir "Numero 2 (Resta)"
	Escribir "Numero 3 (Multiplicacion)"
	Escribir "Numero 4 (Division)"
	Escribir "Ingrese el numero para realizar la operacion a realizar"
	Leer signo 
	Escribir "ingrese segundo valor"
	Leer numero2
	
	calculadora= signo
	si (calculadora =1) Entonces
				Escribir "= ",(numero1+numero2)
			SiNo si(calculadora = 2) Entonces
					Escribir "= ",(numero1 - numero2)
				SiNo
					si (calculadora = 3) Entonces
						Escribir "= ", (numero1 * numero2)
					SiNo
						si (calculadora = 4) Entonces
							Escribir "= ", (numero1 / numero2)
						FinSi
					FinSi
				FinSi
			FinSi
FinAlgoritmo



	

