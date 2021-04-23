from abc import abstractmethod
import random
import string
from src.controllers.short import shortPathController
#modo singleton ...
shortController=shortPathController.ShortPathController()
#interfaz o clase con metodo abstracto
class AlgorithmShort():
    @abstractmethod
    def acortar_url(self):
        pass

#principio 1 unica responsabilidad
#low class
class BaseLowShort():
    #Atributos
    cantidad_caracteres:int

    def __init__(self,cantidad_caracteres):
        self.cantidad_caracteres=cantidad_caracteres
  
    #Metodo abstracto para aplicar el principio 2 de solid Abierto y cerrado
    #@abstrctmethod
    #def get_cantidad_letras(self):
        #pass

    #Metdos de acceso para cumplir con el principio 3 Liskov Substitution
    #def set_nombre_host(self):
        #return self.nombre_host

    #def get_nombre_host(self, nombre_host):
        #self.nombre_host=nombre_host
    

    #Metodo para cumplir con el principio 4 a modo conceptual ..., principio de segregacion de interfaz    
    #@abstractmethod
    #def acortar_url(self):
        #pass
 
 #low level class implementa el metodo abstracto de la clase "AlgorithmShort"

#findurl=findurlShort()

#varBase=BaseLowShort(4,true,findUrl)

#varAcor=AcortadorAlgoBasic(varBase)

#
class AcortadorAlgoBasic(BaseLowShort, AlgorithmShort):

    def __init__(self, base:BaseLowShort):
        self.cantidad_caracteres=base.cantidad_caracteres
    

    def acortar_url(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        rand_letters = random.choices(letters, k=self.cantidad_caracteres)
        rand_letters = "".join(rand_letters)
        return rand_letters


#principio 1 Unica responsabilidad
class FindUrlShort():
    def __init__(self):
        #self.letras_generadas=letras_generadas
        #self.id_user=id_user
        pass
    def findUrl(self,caracteres_generados, id_usuario):
        shortController.get_path(caracteres_generados, id_usuario)

#principio 5-- inversion de dependencias
class ShortUrl():
    #findurl=findurlShort()
    #varBase=BaseLowShort(4,true,findUrl)
    #varAcor=AcortadorAlgoBasic(varBase)
    #Atributos
    algorithm_short:AlgorithmShort
    id_user:int
    session_user:bool
    findurlshort:FindUrlShort
    def __init__(self,algorithm_short,id_user=0,session_user=False,findurlshort=None):
        self.algorithm_short=algorithm_short
        self.id_user=id_user
        self.session_user=session_user
        self.findurlshort=findurlshort
        #objBase=BaseLowShort(5)

    def sol(self):
        while True:
            caracteres_generados=self.algorithm_short.acortar_url()
            if self.session_user:
                findurl=self.findurlshort.findUrl(caracteres_generados,self.id_user)
                if not findurl:
                    return caracteres_generados
            else:
                return caracteres_generados


             


#clase de hight level ...