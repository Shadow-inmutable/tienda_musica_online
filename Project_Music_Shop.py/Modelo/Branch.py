class Sucursal:
    def __init__(self,dir:str,ciu:str,prin:bool):
        self.__direccion=dir
        self.__ciudad=ciu
        self.__principal=prin
        self.empleados=[]
        
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self,dir:str):
        self.__direccion=dir
    
    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self,ciu:str):
        self.__ciudad=ciu
    
    @property
    def principal(self):
        return self.__principal
    @principal.setter
    def principal(self,prin:bool):
        self.__principal=prin
        