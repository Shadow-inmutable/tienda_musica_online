

class Empleado(Persona):
    def __init__(self,doc,nom,ape,cor,tipo,mod,sal:float,dir):
        super().__init__(doc,nom,ape,cor)
        self._tipo=tipo
        self._modulo=mod
        self._salario=sal
        self._dirige=dir
        self._creadas=[]
        
    @property
    def tipo (self):
        return self._tipo

    @tipo.setter
    def tipo(self,tipo):
        self._tipo=tipo
        
    @property
    def modulo(self):
        return self._modulo
    
    @modulo.setter
    def modulo(self,mod):
        self._modulo=mod
    
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,sal):
        self._salario=sal
    
    @property
    def dirige(self):
        return self._dirige
    @dirige.setter
    def dirige(self,dir):
        self.__dirige=dir
            
        
