from Personaje_clase import Personaje

menu = """
########################################
#    1-Crear un personaje              #
#                                      #
#    2- Mostrar lista de personajes    #
#                                      #
#    3- Realizar una carrera           #
#                                      # 
#    4- Salir                          #
########################################
"""
print("Vamos a jugar con diferentes personajes")

while True:
    print(menu)
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        print("Vamos a crear un personaje")
        nombre = input("Ingrese el nombre del personaje:")
        altura = int(input("Ingrese la altura del personaje entre 100 - 200:"))
        velocidad = int(input("Ingrese la velocidad del personaje entre 1 - 10:"))
        resistencia = int(input("Ingrese la resistencia del  personaje entre 1 - 10:"))
        fuerza = int(input("Ingrese la fuerza del personaje entre 1 - 10:"))
        p1=Personaje(nombre, altura, velocidad, resistencia, fuerza)

    elif opcion == 2:
        print(f"Elegiste la opcion {opcion}")
    
    elif opcion == 3:
        print(f"Elegiste la opcion {opcion}")
        tiempoCarrera = p1.correr()
        print(tiempoCarrera)

    elif opcion == 4:
        print(f"Elegiste la opcion {opcion}")
        break
print("FIN")