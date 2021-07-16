class Auto:
    Rojo:False
    def __init__(self,puertas=None,color=None):
        self.puertas= puertas
        self.color = color
        if puertas is not None and color is not None:
            print("se creo un auto con puertas {} y color {}".format(puertas,color))

    def fabricar(self):
        self.Rojo = True
    def confirmar_fabricacion(self):
        if (self.Rojo):
            print('auto fabricado de color rojo')
        else:
            print('aun no esta coloreado')
#a = Auto()
a = Auto('4','Rojo')
