from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Modelo.admin_shop import *
from Controlador.conexion import *
from Controlador.dao_logic import *

#variables globales para el manajo de instancias de las clases importadas
db=DataBase()
dao = Dao(db)

class MiVentanaPrincipal:
    def __init__(self,root):
        self.root=root
        self.root.title('Formulario Principal')
        self.root.config(bg='burlywood')
        self.root.state('zoomed')

        #Controles como atributos
        #espacio para la barra de menu
        self.barraMenu= Menu(self.root)
        self.root.config(menu=self.barraMenu, width=600, height=600)

        #menus dentro de la barra de menu
        self.admin_shopMenu= Menu(self.barraMenu,tearoff=0)
        self.admin_shopMenu.add_command(label='Admon_organizador',command=self.frm_admin_shop)
        self.admin_shopMenu.add_command(label='Salir',command=self.salir)

        #self.ubicacionMenu=Menu(self.barraMenu,tearoff=0)
        #self.ubicacionMenu.add_command(label='Admon_Ubicaciones',command=self.frm_ubicacion)

        #self.proveedorMenu=Menu(self.barraMenu,tearoff=0)
        #self.proveedorMenu.add_command(label='Admon_Proveedores',command=self.frm_proveedor)

        #self.instrumentosMenu=Menu(self.barraMenu,tearoff=0)
        #self.instrumentosMenu.add_command(label='Admon_Equipos',command=self.frm_instrumentos)
        
        #self.accesoriosMenu=Menu(self.barraMenu,tearoff=0)
        #self.accesoriosMenu.add_command(label='Admon_Software',command=self.frm_accesorios)
        
        #self.exibidoresMenu=Menu(self.barraMenu,tearoff=0)
        #self.exibidoresMenu.add_command(label='Admon_Partes',command=self.frm_exibifores)
        
        #self.clientesMenu=Menu(self.barraMenu,tearoff=0)
        #self.clientesMenu.add_command(label='Admon_Partes',command=self.frm_clientes)
        
        #self.productosMenu=Menu(self.barraMenu,tearoff=0)
        #self.productosMenu.add_command(label='Admon_Partes',command=self.frm_productos_aseo)
        
        #self.documentacionMenu=Menu(self.barraMenu,tearoff=0)
        #self.documentacionMenu.add_command(label='Camara y Comerico')
        #self.documentacionMenu.add_command(label='Industria y comercio')
        #self.documentacionMenu.add_command(label='Estudio de suelos')

        self.ayudaMenu=Menu(self.barraMenu,tearoff=0)
        self.ayudaMenu.add_command(label='Acerca de...')
        self.ayudaMenu.add_command(label='Licencia')

        #Agregar opciones a los menus
        self.barraMenu.add_cascade(label='Administradores',menu=self.admin_shopMenu)
        #self.barraMenu.add_cascade(label='Proveedores',menu=self.proveedorMenu)
        #self.barraMenu.add_cascade(label='Ubicaciones',menu=self.ubicacionMenu)
        #self.barraMenu.add_cascade(label='Equipos',menu=self.equipoMenu)
        #self.barraMenu.add_cascade(label='Software',menu=self.softwareMenu)
        #self.barraMenu.add_cascade(label='Parte',menu=self.parteMenu)
        self.barraMenu.add_cascade(label='Ayuda',menu=self.ayudaMenu)

        #Variables vinculadas a los Entry
        self.caja1=StringVar()
        self.caja2=StringVar()
        self.caja3=StringVar()
        self.caja4=StringVar()
        self.caja5=StringVar()
        self.caja6=StringVar()
        self.caja7=StringVar()
        self.caja8=StringVar()
        self.caja9=StringVar()
        self.caja10=StringVar()
        self.caja11=StringVar()
        #Creacion de widgets en las ventanas secundarias
        self.txt_caja1=Entry()
        self.txt_caja2=Entry()
        self.txt_caja3=Entry()
        self.txt_caja4=Entry()
        self.txt_caja5=Entry()
        self.txt_caja6=Entry()
        self.txt_caja7=Entry()
        self.txt_caja8=ttk.Combobox()
        self.txt_caja9=ttk.Combobox()
        self.txt_caja10=ttk.Combobox()
        self.txt_caja11=ttk.Combobox()

        self.btn_nuevo=Button()
        self.btn_buscar=Button()
        self.btn_modificar=Button()
        self.btn_eliminar=Button()
        
    # Metodos de Validacion
    def validar_numeros(self,action,proposed_text,current_text):
        if action == '1':
            if len(current_text) > 12:
                return False
            return proposed_text.idgigit()
        return True
    
    def validar_letras(self,action,proposed_text,current_text):
        if action == '1':
            if len(current_text) > 40:
                return False
            return all(c.isalpha() or c.isspace() for c in proposed_text)
        return True
    
    def validar_fecha(self,fecha):
        if len(fecha) >10: 
            return False
        valores=[]
        for i,char in enumerate(fecha):
            if i in (4,7):
                valores.append(char=='-')
            else:
                valores.append(char.isdigit())
        return all(valores)
    
    
        
    def salir(self):        
        rta=messagebox.askquestion('Salir','Desea salir de la aplicación?')
        if rta=='yes':
            self.root.destroy()

    def frm_admin_shop(self):
        ventana= Toplevel(self.root)
        ventana.title('Administración de tienda')
        ventana.config(width=500,height=500)

        # Para los controles se adapten mejor a la ventana
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=25)
        ventana.columnconfigure(1, weight=2)
        ventana.rowconfigure(1, weight=1)

        frame1= Frame(ventana,bg='gray15')
        frame1.grid(row=0,column=0, sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=1,columnspan=1, sticky='nsew')

        
        lbl_id=Label(frame1,text='id',width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1,state='readonly')
        self.txt_caja1.grid(row=0,column=1)

        lbl_documento=Label(frame1,text='Documento',width=15)
        lbl_documento.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2,
                             validate='key',validatecommand=(ventana.register(self.validar_numeros),'%d','%S','%P'))
        self.txt_caja2.grid(row=1,column=1)
        self.txt_caja2.focus()
        

        lbl_nombres=Label(frame1,text='Nombres',width=15)
        lbl_nombres.grid(row=2,column=0,padx=10,pady=10)
        self.txt_caja3=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja3,
                             validate='key',validatecommand=(ventana.register(self.validar_letras),'%d','%S','%P'))
        self.txt_caja3.grid(row=2,column=1)

        lbl_apellidos=Label(frame1,text='Apellidos',width=15)
        lbl_apellidos.grid(row=3,column=0,padx=10,pady=10)
        self.txt_caja4=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja4,
                             validate='key',validatecommand=(ventana.register(self.validar_letras),'%d','%S','%P'))
        self.txt_caja4.grid(row=3,column=1)

        lbl_correo=Label(frame1,text='Correo',width=15)
        lbl_correo.grid(row=4,column=0,padx=10,pady=10)
        self.txt_caja5=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja5)
        self.txt_caja5.grid(row=4,column=1)

        lbl_telefono=Label(frame1,text='Telefono',width=15)
        lbl_telefono.grid(row=5,column=0,padx=10,pady=10)
        self.txt_caja6=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja6)
        self.txt_caja6.grid(row=5,column=1)
        
        lbl_direccion=Label(frame1,text='Dirección',width=15)
        lbl_direccion.grid(row=5,column=0,padx=10,pady=10)
        self.txt_caja7=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja7)
        self.txt_caja7.grid(row=5,column=1)
        
        #Colocar los botones en frame 2
        self.btn_nuevo= Button(frame2,width=10,font=('Arial',12,'bold'),text='Nuevo',bg='purple',bd=5,command=self.crear_admin_shop_v)
        self.btn_nuevo.grid(row=0,column=0,padx=10,pady=10)

        self.btn_buscar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Buscar',bg='purple',bd=5,command=self.buscar_admin_shop_v)
        self.btn_buscar.grid(row=0,column=1,padx=10,pady=10)

        self.btn_modificar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Modificar',bg='purple',bd=5,command=self.modificar_admin_shop_v)
        self.btn_modificar.grid(row=0,column=2,padx=10,pady=10)

        self.btn_eliminar= Button(frame2,width=10,font=('Arial',12,'bold'),text='Eliminar',bg='purple',bd=5,command=self.eliminar_admin_shop_v)
        self.btn_eliminar.grid(row=0,column=3,padx=10,pady=10)

        ventana.focus()
        self.txt_caja2.focus()
        ventana.grab_set()
    
    def crear_admin_shop_v(self):
        if self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() and self.caja7.get() !='':
            obj_admin_shop=Administrador(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja7.get())
            dao.crear_admin_shop(obj_admin_shop)
            self.limpiar()
        else:
            messagebox.showerror('Error','Todos los campos son obligatorios...')
    
    def buscar_admin_shop_v(self):
        if self.caja2.get() != '':
            administrador= dao.buscar_admin_shop(self.caja2.get())
            if administrador != None:
                obj_adm=Administrador(administrador[1],administrador[2],administrador[3],administrador[4],administrador[5],administrador[6],administrador[7],administrador[0])
                self.caja1.set(obj_adm.id_admin)
                self.caja2.set(obj_adm.documento)
                self.caja3.set(obj_adm.nombres)
                self.caja4.set(obj_adm.apellidos)
                self.caja5.set(obj_adm.correo)
                self.caja6.set(obj_adm.telefono)
                self.caja7.set(obj_adm.direccion)
                
            else:
                messagebox.showwarning('No encontrado','Registro no encontrado...')
        else:
            messagebox.showwarning('No encontrado','debe enviar un criterio de busqueda...')

    def modificar_admin_shop_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() and self.caja7.get() !='':
            obj_cuentadante= Administrador(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja7.get(),self.caja1.get())
            dao.modificar_cuentadante(obj_cuentadante)
            self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def eliminar_admin_shop_v(self):
        if self.caja1.get() and self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() and self.caja7.get() !='':
            obj_cuentadante= Administrador(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get(),self.caja7.get(),self.caja1.get())
            res=dao.eliminar_cuentadante(obj_cuentadante)
            if res:
                self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')

    def limpiar(self):
        self.caja1.set('')
        self.caja2.set('')
        self.caja3.set('')
        self.caja4.set('')
        self.caja5.set('')
        self.caja6.set('')
        self.caja7.set('')
        self.caja8.set('')
        self.caja9.set('')
        self.caja10.set('')
        self.caja11.set('')
        self.txt_caja2.focus()
    