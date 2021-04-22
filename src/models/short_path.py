from src.config.settings import db
from src.dto.short_path import ShortPathDTO
from sqlalchemy.sql import select

class ShortPath(db.Model):
    __tablename__='short_path'
    id=db.Column(db.Integer, primary_key=True)
    path=db.Column(db.String(255), nullable=False)
    pathShort=db.Column(db.String(255), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    parent=db.relationship("User", back_populates="children")

    def json(self):
        return {
            'id':self.id,
            'path':self.path,
            'pathShort':self.pathShort,
            'user_id':self.user_id
        }
    
    def add_path(self, shortPath:ShortPathDTO):
        new_path_short=ShortPath(path=shortPath.path, pathShort=shortPath.pathShort, user_id=shortPath.user_id)
        db.session.add(new_path_short)
        db.session.commit()

    def get_path_short_by_user(self, path_short, id_user):
        query_result=ShortPath.query.filter_by(pathShort=path_short,user_id=id_user).first()
        return query_result

    def get_path_by_user(self,path_, id_user):
        query_result=ShortPath.query.filter_by(path=path_,user_id=id_user).first()
        return query_result

    def get_path_by_id(self,id_):
        query_result=ShortPath.query.filter_by(id=id_).first()
        return query_result

    def get_all_by_user(self,_id):
        query_resolve = ShortPath.query.filter(
            ShortPath.user_id.like(_id),
        )
        return query_resolve; 

    def delete_path(self, id_path, id_user_):
        d = ShortPath.query.filter_by(id=id_path,user_id=id_user_).delete()
        db.session.commit()
        return d 

    def update_path(self, path, _id):
        path_update = ShortPath.query.filter_by(id=_id).first()
        path_update.path=path 
        db.session.commit()

db.create_all()
db.session.commit()