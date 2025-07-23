from Personaje_clase import Personaje

print("Vamos a jugar")

#nombre, altura, velocidad, resistencia, fuerza
p1 = Personaje("Pepe", 180, 80, 90, 7)
p2 = Personaje("Luis", 190, 60, 70, 8)

print(f"la resistencia de {p1.nombre} es {p1.resistencia}")
print(f"la resistencia de {p2.nombre} es {p2.resistencia}")

danho = p1.atacar(50)
print(f"el daño recibido es {danho}")

print(f"la resistencia de {p2.nombre} quedo {p2.recibir_dano(danho)}")

print("FIN")