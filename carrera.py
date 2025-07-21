from Personaje_clase import Personaje


print("Vamos a crear un personaje")
nombre = input("Ingrese el nombre del personaje:")
altura = int(input("Ingrese la altura del personaje entre 100 - 200:"))
velocidad = int(input("Ingrese la velocidad del personaje entre 1 - 10:"))
resistencia = int(input("Ingrese la resistencia del  personaje entre 1 - 10:"))
fuerza = int(input("Ingrese la fuerza del personaje entre 1 - 10:"))

p1 = Personaje(nombre, altura, velocidad, resistencia, fuerza)
print(p1)

print("Vamos a crear otro personaje")
nombre = input("Ingrese el nombre del personaje:")
altura = int(input("Ingrese la altura del personaje entre 100 - 200:"))
velocidad = int(input("Ingrese la velocidad del personaje entre 1 - 10:"))
resistencia = int(input("Ingrese la resistencia del  personaje entre 1 - 10:"))
fuerza = int(input("Ingrese la fuerza del personaje entre 1 - 10:"))

p2 = Personaje(nombre, altura, velocidad, resistencia, fuerza)
print(p2)

print(f"Vamos a jugar una carrera entre {p1} y {p2}, veremos como sale")

tiempoCarrera = p1.correr()
print(tiempoCarrera)