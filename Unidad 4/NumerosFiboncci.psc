Algoritmo NumerosFibonacci
	Definir N1 como Entero  
	Definir a Como Entero
	Definir b Como Entero
	Definir c Como Entero
	
	Escribir  "Ingrese el numero de fibonacci a resolver"
	Leer N1
	
	a = 0
	b =1
	c =1
	
	
	si N1 <= 0 Entonces 
		Escribir "El resultado es 0"
		sino 
			Para f <- 1 hasta N1 Hacer
		
			c <- a + b
			a <- b
			b <- c
			
		FinPara
		Escribir "El resultado es ", a
	finsi
	
FinAlgoritmo
