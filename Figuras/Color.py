'''
    Color.py
'''
#creación de la clase
class Color:
    #constructor
    def __init__(self,color:str) -> str:
        #-----Atributo------#
        self.__color = color
    #-----Metodos--------#
    @property
    def color(self):
        return  self.__color

    @color.setter
    def color(self,color):
        self.__color = color

    def __str__(self):
        return  f"Color[color: {self.__color}]"