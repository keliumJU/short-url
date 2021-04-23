from acortador import AcortarUrl
#principio 2 abierto y cerrado
class ModCantidadLetras(AcortarUrl):
    def __init__(self, cantidad_letras):
        self.cantidad_letras = cantidad_letras

    def changeCant(self):
        return self.cantidad_letras + 5