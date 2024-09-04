class Persona:
    def __init__(self,doc,nom,ape,cor):
        self._documento=doc
        self._nombres=nom
        self._apellidos=ape
        self._email=cor
    
    
    @property
    def documento(self):
        return self._documento
    @documento.setter
    def id(self,doc:str):
        self._documento=doc
    
    @property
    def nombres(self):
        return self._nombres
    @nombres.setter
    def nombres(self,nom:str):
        self._nombres=nom
    @property
    def apellidos(self):
        return self._apellidos
    @apellidos.setter
    def apellidos(self,ape:str):
        self._apellidos=ape
        
    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo (self,cor:str):
        self._correo=cor