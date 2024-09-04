#Persona encargada de los Instrumentos

class cuentadante:
    def __init__(self,doc,nom,ape,email,phone,id=None):
        self.documento=doc
        self.nombres=nom
        self.apellidos=ape
        self.correo=email
        self.telefono=phone
        self.id=id
        
@property
def documento(self):
    return self.documento
@documento.setter
def documento(self,doc):
    self.documento=doc

@property
def nombres(self):
    return self.nombres
@nombres.setter
def nombres(self,nom):
    self.nombres=nom
    
@property
def apellidos(self):
    return self.apellidos
@apellidos.setter
def apellidos(self,ape):
    self.apellidos=ape

@property
def correo(self):
    return self.coreo
@correo.setter
def correo(self,email):
    self.correo=email

@property
def telefono(self):
    return self.telefono
@telefono.setter
def telefono(self,phone):
    self.telefono=phone

@property
def id(self):
    return self.id
@id.setter
def id(self,id):
    self.id=id

    