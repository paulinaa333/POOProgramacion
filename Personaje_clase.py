class Personaje():

    estado = True

    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        if altura < 100 or altura > 200:
            raise ValueError("La altura debe estar entre 100 y 200")
        self.velocidad = velocidad
        if velocidad < 1 or velocidad > 10:
            raise ValueError("La velocidad debe estar entre 1 y 10")
        self.resistencia = resistencia
        if resistencia < 1 or resistencia > 10:
            raise ValueError("La resistencia debe estar entre 1 y 10")
        self.fuerza = fuerza
        if fuerza < 1 or fuerza > 10:
            raise ValueError("La fuerza debe estar entre 1 y 10") 
        print(f"se creo personaje {self.nombre}")

    def atacar(self, otro_personaje):
        cantidad = otro_personaje - self.fuerza
        return cantidad
    
    def recibir_dano(self, cantidad):
        self.resistencia = self.resistencia - cantidad

    def correr (self):
        distancia = 1000
        cansancio = (distancia / self.resistencia)*2
        tiempo = distancia / (self.velocidad - cansancio)
        print(tiempo)

    def mostrar_info(self):
        return f"Personaje: {self.nombre}, Altura: {self.altura}, Velocidad: {self.velocidad}, Resistencia: {self.resistencia}, Fuerza: {self.fuerza}"