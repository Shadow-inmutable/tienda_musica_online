class Administrador:
    def __init__(self,doc,nom,ape,cor,tel,dir,id=None):
        self.__documento=doc
        self.__nombres=nom
        self.__apellidos=ape
        self.__correo=cor
        self.__telefono=tel
        self.__direccion=dir
        self.__id_admin=id
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self,doc):
        self.__documento= doc
    
    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self,nom):
        self.__nombres=nom
    
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self,ape):
        self.__apellidos=ape

    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self,cor):
        self.__correo= cor
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,tel):
        self.__telefono= tel
                
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,dir):
        self.__direccion=dir
    
    @property
    def id_admin(self):
        return self.__id_admin
    
    @id_admin.setter
    def id_admin(self,id):
        self.__id_admin= id