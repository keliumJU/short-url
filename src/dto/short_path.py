class ShortPathDTO():
    path:str
    pathShort:str
    user_id:int
    def __init__(self,path,pathShort,user_id):
        self.path=path
        self.pathShort=pathShort
        self.user_id=user_id