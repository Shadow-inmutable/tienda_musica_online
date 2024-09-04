from modelo.Branch import Sucursal
from modelo.employee import Empleado

class tienda_Musica:
    def __init__(self,nit:str,nom:str,ofi:Sucursal,rep:Empleado):
        self.__nit=nit
        self.__nombre=nom
        self.__oficina=ofi if isinstance (ofi,Sucursal) else None
        self.__representante=rep if isinstance (rep,Empleado) else None
        self.__sucursales=[]
        
    '''def get_nit(self):
            return self.__nit
        def self_nit(self,nit:str):
            self.__nit=nit'''
    
    @property
    def nit (self):
        return self.__nit
    @nit.setter
    def nit(self,nit:str):
        self.__nit=nit
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom:str):
        self.__nombre=nom
    @property
    def oficina(self):
        return self.__oficina
    @oficina.setter
    def oficina(self,ofi:Sucursal):
        self.__oficina=ofi
    @property
    def representante(self):
        return self.__representante
    @representante.setter
    def representante (self,rep:Empleado):
        self.__representante=rep
        
    @property
    def sucursales(self):
        return self.__sucursales
    
    def agregar_sucursal(self,suc:Sucursal):
        existe=self.validar_sucursal (suc)
        if not existe:
            self.sucursales.append(suc) if isinstance (suc,Sucursal) else None
        else:
            print('No puede registrar sucursales con la misma direccion')
        
    def validar_sucursal(self,suc: Sucursal):
        for i in self.__sucursales:
            if suc.direccion == i.direccion:
                return True
        return False