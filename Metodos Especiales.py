class fabrica:
    def __init__(self,tiempo,nombre,ruedas):
        self.tiempo=tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print('se creo el auto', self.nombre)

    def __del__(self):
        print('se elimino el auto',self.nombre)

    def __str__(self):
        return "{} se fabrico con exito, en el tiempo {} y tiene esta cantidad de ruedas {}".format(self.nombre,self.tiempo,self.ruedas)

    def __len__(self):
        return self.tiempo

a = fabrica(10,'Forsh',4)
print(len(a))