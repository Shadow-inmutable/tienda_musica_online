import mysql.connector
#from mysql.connector.errors import Error
from mysql.connector import Error
from tkinter import messagebox
from Modelo.admin_shop import *

class Dao:
    def __init__(self,db):
        self.db=db
    
    #CRUD Cuentadante
    
    def crear_admin_shop(self,obj:Administrador):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular)
        insert='insert into cuentadante(documento,nombres,apellidos,correo,celular) values (%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo Registro','El cuentadante ha sido almacenado...')
        except mysql.connector.Error as e:
            messagebox.showinfo('Nuevo Registro',e)
    
    def buscar_admin_shop(self,doc):
        criterio=(doc,)
        select='select * from admin_shop where documento= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_cue= self.db.cursor.fetchone()
            return obj_cue
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def buscar_cuentadante_1(self,nom,ape):
        val=(nom,ape)
        select='select * from admin_shop where nombres= %s and apellidos=%s'
        try:
            self.db.cursor.execute(select,val)
            obj_cue= self.db.cursor.fetchone()
            return obj_cue
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_cuentadante(self,obj:Administrador):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular,obj.id)
        update='update cuentadante set documento= %s, nombres= %s, apellidos=%s, correo=%s, celular=%s where id= %s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
        
    def eliminar_cuentadante(self,obj:Administrador):
        mensaje='Esta seguro de eliminar el registro?'
        valor= messagebox.askquestion('Eliminar',mensaje)
        if valor == 'yes':
            delete='delete from cuentadante where id= %s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado...')
                return True
            except mysql.connector.Error as e:
                messagebox.showinfo('Eliminar',e)
                return False
    