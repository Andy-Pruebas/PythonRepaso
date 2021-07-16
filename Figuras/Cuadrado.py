'''
    Cuadrado.py
'''
#------------Importación de modulos-------------#
from FiguraGeometrica import FiguraGeometica
from Color import Color

#creación de clase
class Cuadrado(FiguraGeometica,Color):
    #constructor
    def __init__(self,lado, color):

        #-------Atributos-------#
        FiguraGeometica.__init__(self,lado,lado)
        Color.__init__(self,color)

    #-----Metodos------#
    def calcular_area(self):
        return self.base * self.altura

    def __str__(self):
        return f"{FiguraGeometica.__str__(self)} {Color.__str__(self)}"