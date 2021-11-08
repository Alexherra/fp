"""Determinar si un alumno reprobo o aprobo."""
Cal1 = float(input("ingresar la calificacion 1:"))
Cal2 = float(input("ingresar la calificacion 2:"))

Promedio = (Cal1 + Cal2) / 2

if promedio >= 60:
    print("Aprobaste con un promedio de ",round(Promedio,1))
else:
    print(" Reprobaste con un promedio de ",round(Promedio,1))