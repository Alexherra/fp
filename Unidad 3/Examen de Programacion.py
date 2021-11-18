#Programa que guarde a todos los integrantes del grupo como objetos

'''Crear una clase'''
class Alumno():
 	def __init__ (self,Nombre,Edad,Fundamentos Investigacion,Introduccion TICs,Ingles, Calculo Diferencial,Matematicas Discretas,Taller Etica,Fundamentos Programacion,Promedio,Calificacion Prepa,Lugar Residencia, Distancia):
 		self.Nombre = Nombre
 		self.Edad = Edad
 		self.Fundamentos Investigacion = Fundamentos Investigacion
 		self.Introduccion TICs = Introduccion TICs
 		self.Ingles = Ingles
 		self.Calculo Diferencial = Calculo Diferencial
 		self.Matematicas Discretas = Matematicas Discretas
 		self.Taller Etica = Taller Etica
 		self.Fundamentos Programacion = Fundamentos Programacion
 		self.Promedio = Promedio
 		self.Calificacion Prepa = Calificacion Prepa
 		self.Lugar Residencia = Lugar Residencia
 		self.Distancia = Distancia

'''Crear un objeto'''
Reyna = Alumno("Reyna", 18, 7, 8, 9, 8, 10, 9, 10, 87, 9, "Emiliano Zapata", 13)
Sharlene = Alumno("Sharlene", 18,8, 9, 9, 8, 10, 9, 8, 87, 8, "Cosio", 27)
Melany = Alumno ("Melany", 18, 9, 8, 10, 8, 7, 8, 9, 84, 7, "Pabellon", 5)
Diego = Alumno("Diego", 18, 8, 9, 9, 10, 8, 8, 10, 88, 9, "Rincon", 13) 
Britzy = Alumno("Britzy", 18, 8, 7, 9, 9, 9, 10, 8, 85, 8, "Rincon", 13) 
Fernando = Alumno("Fernando", 17, 9, 10, 9, 8, 7, 10, 9, 88, 9, "Pabellon", 5)
Johana = Alumno("Johana", 18, 9, 10, 8, 8, 7, 8, 9, 84, 9, "Jesus Maria", 27)
Alejandro= Alumno("Alejandro", 19, 10, 9, 9, 10, 9, 10, 8, 92, 10, "Ejido Fresnillo", 17)
Donaldo= Alumno("Donaldo", 18, 9, 8, 8, 8, 9, 10, 7, 84, 9, "Pabellon", 5)
Austin= Alumno("Austin", 18, 9, 9, 9, 8, 8, 10, 9, 88, 8, "Pabellon", 5)
Paola=Alumno("Paola", 18, 9, 9, 7, 10, 8, 9, 9, 87, 9, "Carboneras", 8)
Isaac=Alumno("Isaac", 19, 9, 10, 9, 8, 8, 9, 7, 85, 9, "Rincon", 13)
Areli=Alumno("Areli", 19, 9, 8, 7, 8, 9, 10, 9, 85, 8, "Rincon", 13)
Elias=Alumno("Elias", 18, 10, 8, 7, 9, 10, 8, 9, 87, 8, "Asientos", 11)
Alexis=Alumno("Alexis", 19, 7, 7, 7, 6, 5, 5, 5, 60, 7, "Rincon", 13)

'''Alumnos con mayor edad'''
print("Alumnos con mayor edad son", Alejandro.Nombre,",",Isaac.Nombre,",",Areli.Nombre,",",Alexis.Nombre,",",Diego.Nombre)

'''Promedios de preparatoria'''
print("Promedio de los Alumnos en Preparatoria\n", Reyna.Nombre,"Promedio de",Reyna.Calificacion Prepa,",\n",Sharlene.Nombre,"Promedio de",Sharlene.Calificacion Prepa,Melany.Nombre,"Promedio de",Melany.Calificacion Prepa)
print(Diego.Nombre,"Promedio de",Diego.Calificacion Prepa,",\n",Britzy.nombre,"Promedio de",Britzy.Calificacion Prepa)
print(Fernando.Nombre,"Promedio de",Fernando.Calificacion Prepa,",\n",Johana.Nombre,"Promedio de",Johana.Calificacion Prepa,",\n",Alejandro.Nombre,"Promedio de",Alejandro.Calificacion Prepa,Donaldo.Nombre,"Promedio de",Donaldo.Calificacion Prepa)
print(Austin.Nombre,"Promedio de",Austin.Calificacion Prepa,",\n",Paola.Nombre,"Promedio de",Paola.Calificacion Prepa)
print(Isaac.Nombre,"Promedio de",Isaac.Calificacion Prepa,",\n",Areli.Nombre,"Promedio de",Areli.Calificacion Prepa,",\n",Elias.Nombre,"Promedio de",Elias.Calificacion Prepa,",\n",Alexis.Nombre,"Promedio de",Alexis.Calificacion Prepa)

'''Alumnos que viven mas lejos y mas cerca'''
print("Los Alumnos que viven mas cercas son:\n", Melany.Nombre,"Con unos",Melany.Distancia,"Kilometros",",",Fernando.Nombre,"Con unos",Fernando.Distancia,",",Donaldo.Nombre,"Con unos",Donaldo.Distancia,",",Austin.Nombre,"Con unos",Austin.Distancia,"Kilometros")
print("Los Alumnos que viven mas lejos son:\n", Alejandro.Nombre,"Con unos",Alejandro.Distancia,"Kilometros",","Sharlene.Nombre,"Con unos",Sharlene.Distancia,"Kilometros",",",Johana.Nombre,"Con unos",",",Johana.Distancia,"Kilometros")

'''Materias con mejor rendimineto de los alumnos'''
print("Las materias con mejor rendimiento de los Alumnos son:\n", Reyna.Nombre,"en Matematicas Discretas con una calificacion de",Reyna.Matematicas Discretas,",\n",Sharlene.Nombre,"en Matematicas Discretas con una calificacion de",Sharlene.Matematicas Discretas)
print(Melany.Nombre,"en Ingles con una calificacion de",Melany.Ingles,",\n",Diego.Nombre,"en Calculo Diferencial con una calificacion",Diego.Calculo Diferencial,",\n",Britzy.nombre,"en Taller de etica con una calificacion de",Britzy.Taller Etica)
print(Fernando.Nombre,"en Introduccion a TICs con una calificaicon de",Fernando.Introduccion TICs,"y Taller de etica con calificaicon de",Fernando.Taller Etica,",\n",Johana.Nombre,"en Introduccion a TICs Con una calificacion de",Johana.Introduccion TICs)
print(Alejandro.Nombre,"en Fundamentos de Investigacion con una calificacion de",Alejandro.Fundamentos Investigacion,",","en Calculo Diferencial con una calificacion de", Alejandro.Calculo Diferencial,"y en Taller de etica con una calificacion de",Alejandro.Taller Etica)
print(Donaldo.Nombre,"en Taller de etica con una calificacion de",Donaldo.Taller Etica,",\n",Austin.Nombre,"en Taller de etica con una calificacion de",Austin.Taller Etica,",\n",Paola.Nombre,"en Calculo Diferencial con una calificacion de",Paola.Calculo Diferencial)
print(Isaac.Nombre,"en Introduccion a TICs con una calificaicon de",Isaac.Introduccion TICs,",\n",Areli.Nombre,"en Taller de etica con una calificacion de",Areli.Taller Etica)
print(Elias.Nombre,"en Fundamentos de Investigacion con una calificacion de",Elias.Fundamentos Investigacion,"y en Matematicas Discretas con una calificacion de",Elias.Matematicas Discretas)
print(Alexis.Nombre,"en Fundamentos de Investigacion con una calificacion de",Alexis.Fundamentos Investigacion,",","en Introduccion a TICs con una calificacion de", Alejandro.Introduccion TICs,"y en Ingles con una calificacion de",Alexis.Ingles)