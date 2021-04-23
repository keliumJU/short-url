import random
import string

from acortador import AcortarUrl

#clase que implementa el metodo abstracto que se va ha utilizar en la clase AcortadorAlgoBasic
class AlgorithShort():
       #Metodo para cumplir con el principio 4 a modo conceptual ..., principio de segregacion de interfaz    
    @abstractmethod
    def acortar_url(self):
        pass

#principio 4
#En base al principio de segregacion de interfaz al heredar de la interfaz AlgoritShort que solo define un metodo abstracto
# El cual sera implementado por nuestra clase AcortadorAlgoBasic por lo tanto solamente heredamos la interfaz AlgorithShor
# de esta forma no implementamos metodos que no son necesarios para nuestra clase AcortadorAlgoBasic 
class AcortadorAlgoBasic(AlgorithShort):
    def acortar_url(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        while True:
            rand_letters = random.choices(letters, k=cantidad_letras)
            rand_letters = "".join(rand_letters)
            if "user" in session:
                short_url = ShortPath().get_path_short_by_user(rand_letters,session["id"]) 
            else:
                return rand_letters

            if not short_url:
                return r
