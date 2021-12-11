Algoritmo Area
	Definir radio Como Entero
	Definir lado Como Entero
	Definir base1 Como Entero
	Definir altura1 Como Entero
	Definir base2 Como Entero
	Definir altura2 Como Entero
	Definir F Como Caracter
	
	Escribir "--Programa que saca área de figuras (circulo,cuadrado,rectangulo y triangulo)--" 
	Escribir "Ingrese la figura con minusculas para sacar el area"
	Leer F
	
	Repetir
		
		si (F=="circulo") Entonces
			Escribir "Ingrese el radio"
			Leer radio
			Escribir "El area del circulo es: ",radio*radio*pi	
			Escribir "Ingrese alguna otra figura para continuar o ingrese finalizar para terminar"
			Leer F
			Sino Si (F=="cuadrado") Entonces
					Escribir "Ingrese el tamaño del lado"
					Leer lado
					Escribir "El are del cuadrado es: ",lado*lado
					Escribir "Ingrese alguna otra figura para continuar o ingrese finalizar para terminar"
					Leer F
				Sino si (F=="rectagulo") Entonces
						Escribir "Ingrese el tamaño de la base"
						Leer base1
						Escribir "Ingrese el tamaño de la altura" 
						Leer altura1
						escribir "El area del rectamgulo es: ", base1*altura1
						Escribir "Ingrese alguna otra figura para continuar o ingrese finalizar para terminar"
						Leer F
					SiNo si(F=="triangulo") Entonces
							Escribir "Ingrese la altura del triangulo"
							Leer altura2
							Escribir "Ingresar la base del triangulo"
							Leer base2
							Escribir "El area del triangulo es: ", altura2*base2/2
							Escribir "Ingrese alguna otra figura para continuar o ingrese finalizar para terminar"
							Leer F
						FinSi
						
					finsi
			FinSi
		FinSi
		
hasta que F="finalizar"
	
	
FinAlgoritmo
