from src.controllers.short import shortPathController
#modo singleton ...
shortController=shortPathController.ShortPathController()
#principio 1 Unica responsabilidad
class findUrlShort():
    letras_generadas:str
    id_user:int
    def __init__(self,letras_generadas,id_user):
        self.letras_generadas=letras_generadas
        self.id_user=id_user
    def findUrl(self):
        shortController.get_path(self.letras_generadas, self.id_user)