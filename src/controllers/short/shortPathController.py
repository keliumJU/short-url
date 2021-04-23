
#dto, modelo
from src.models.short_path import ShortPath
from src.dto.short_path import ShortPathDTO


class ShortPathController():
    def create(self,shortdto:ShortPathDTO):
        #shortdto=ShortPathDTO(url_received, _id_user)
        ShortPath().add_path(shortdto)

    def list(self, _id_user):
        return ShortPath().get_all_by_user(_id_user)

    def get(self, url_received, _id_user):
        return ShortPath().get_path_by_user(url_received,_id_user) 

    def update(self):
        pass
    def delete(self):
        pass
    
    def get_path(self,rand_letters, id_user):
        return ShortPath().get_path_short_by_user(rand_letters,id_user) 