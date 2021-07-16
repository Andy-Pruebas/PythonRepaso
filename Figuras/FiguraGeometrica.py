''''
FiguraGeometica.py
'''
#creaación de la clase
class FiguraGeometica:
    #constructor

    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura

    #-----Metodos------#

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self,base):
        self.__base = base

    @property
    def altura(self):
        return  self.__altura

    @altura.setter
    def altura(self,altura):
        self.__altura = altura

    def __str__(self):
        return f"Figura Geometrica [Base: {self.__base}, Altura: {self.__altura}]"

