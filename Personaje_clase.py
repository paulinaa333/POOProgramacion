class Personaje():
    estado = True

    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza

    def correr(self):
        #La carrera sera por distancia

        distancia = int(input("Ingrese la distancia de la carrera:"))
        #cansancio = (distancia/self.resistencia) ** 2
        tiempo = distancia / (self.velocidad) #calcular
        print(tiempo)