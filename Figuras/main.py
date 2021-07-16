'''
    Main.py
'''
#--------Importacion de modulos---------#
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

#---------Variables y petición de datos-----------#
print("\n-----Creando el objeto cuadrado------")
lado = int(input("Ingrese el lado del cuadro: "))
colorCuadrado = input("Ingrese el color del cuadrado: ")

print("\n-----Creando un rectangulo------")
base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura de el rectangulo: "))
colorRectangulo  = input("Ingrese el color del rectangulo: ")

#----------Creando Objetos------------#
cuadrado= Cuadrado(lado,colorCuadrado)
rectangulo= Rectangulo(base,altura,colorRectangulo)

#----------Salido de datos-----------#
print("\n----Cuadrado----")
print(f"Calculo del area: {cuadrado.calcular_area()}")
print(cuadrado)

print("\n----Rectangulo----")
print(f"Calculo del area: {rectangulo.calcular_area()}\n")
print(rectangulo)