import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from vista.ventana_admin import Admin, menu_panel_admin

# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 500 , height = 500)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade (label='Salir', command=root.destroy)
#-----------------------------------------------

class Aplicacion (tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=1000, height=600, bg=PRIMARY)
        self.root = root
        self.id_paciente = None
        self.pack()
       
        self.titulo()
        self.grafica()    
    #--------------------------------
    # --> Etiquetas Label
    def titulo(self):
        self.etiqueta_titulo = tk.Label(self, text= "✰ Centro de Estética ✰", font=("Nunito", 35,  "bold"), fg=TITULOS, bg=PRIMARY)
        self.etiqueta_titulo.place(x=235, y=45 )
    #--------------------------------    
    # --> IMAGEN --
    def grafica(self):
        imagen = Image.open("./vista/avatar.jpg")  #guardo en una variable y abro la imagen q está en misma carpeta
        imagen = imagen.resize((150,150))  #le doy nuevo tamaño (formato tupla: x,y)
        
        self.imagen = ImageTk.PhotoImage(imagen)                      #al atributo self.imagen lo abro como clase ImageTk
        self.label_img = tk.Label(self, image=self.imagen)   #indico donde se abre el label y le paso la direccion= imagen
        self.label_img.place(x=580, y=210)                            #ubico la imagen con posicion fija, porque la ventana no se redimensiona
        
        self.imagen2 = ImageTk.PhotoImage(imagen)
        self.label_img2 = tk.Label(self, image=self.imagen2)
        self.label_img2.place(x=280, y=210)

        self.boton_1 = tk.Button(self, text="Usuario",
                                 font=('Nunito', 20, 'bold'),
                                 fg='white',
                                 bg='#805AD5',
                                 activebackground= TITULOS,activeforeground='white',
                                 cursor="hand2",
                                 command= self.elige_usuario)
        self.boton_1.place(x=565, y=400, width=180, height=35)   
      
        self.boton_2 = tk.Button(self, text="Admin",
                                 font=('Nunito', 20, 'bold'),
                                 fg='white',
                                 bg='#805AD5',
                                 activebackground= TITULOS,activeforeground='white',
                                 cursor="hand2",
                                 command= self.elige_admin)
        self.boton_2.place(x=265, y=400, width=180, height=35)
    #--------------------------------
    def elige_admin(self):
        self.root.iconify()     # iconify pone en segunda posicion a la ventana actual.-
        
        self.ventana_admin = tk.Toplevel(self.root)  #toplevel indica que se abre una nueva ventana que depende de la ventana principal
        self.ventana_admin.title("Admin")
        self.ventana_admin.config(bg=TITULOS)
        self.ventana_admin.geometry("1000x600+160+50")
        self.ventana_admin.resizable(0,0)

        # --> menú
        menu_admin = tk.Menu(self.ventana_admin)
        self.ventana_admin.config(menu = menu_admin, width = 500 , height = 500)
        menu_ventana_admin = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade (label='Cerrar', command=self.ventana_admin.destroy)

        # --> imagen
        imagen_admin = Image.open("./vista/avatar.jpg")  
        imagen_admin = imagen_admin.resize((150,150))  #le doy nuevo tamaño (formato tupla: x,y)
        
        self.imagen_admin = ImageTk.PhotoImage(imagen_admin)                
        self.label_img_admin = tk.Label(self.ventana_admin, image=self.imagen_admin)   #indico donde se abre el label y le paso la direccion= imagen
        self.label_img_admin.place( x=415, y=150)  

        # --> etiqueta label
        self.clave_label = tk.Label(self.ventana_admin)
        self.clave_label.config( text='Contraseña: ', 
                                 font= ('Nunito', 20, 'bold'),
                                 fg='white',
                                 bg=TITULOS)
        self.clave_label.place(x=410, y=350)

        # --> entry de contraseña
        self.clave_admin = tk.StringVar()
        self.clave_admin = tk.Entry(self.ventana_admin)
        self.clave_admin.config(font=('Nunito', 19),
                                  width=13,
                                  show='*',
                                  textvariable = self.clave_admin)
        self.clave_admin.place(x=399, y=400)

        # --> botón
        self.boton_ingresar = tk.Button(self.ventana_admin)
        self.boton_ingresar.config(text='Iniciar Sesión',
                             font=('Nunito', 14, 'bold'),
                             width=12,
                             fg='white',
                             bg='#805AD5',
                             cursor="hand2",
                             command= self.ingreso_admin) 
        self.boton_ingresar.place(x=418, y=465)  

        self.ventana_admin.mainloop()
    #--------------------------------
    def elige_usuario(self):
        self.root.iconify()                  # iconify pone en segunda posicion a la ventana actual.-
        
        self.ventana_usuario = tk.Toplevel(self.root)  #toplevel indica que se abre una nueva ventana que depende de la ventana principal
        self.ventana_usuario.title("Usuario")
        self.ventana_usuario.config(bg=TITULOS)
        self.ventana_usuario.geometry("1000x600+160+50")
        self.ventana_usuario.resizable(0,0)

        # --> menú
        menu_usuario = tk.Menu(self.ventana_usuario)
        self.ventana_usuario.config(menu = menu_usuario, width = 500 , height = 500)
        menu_ventana_usuario = tk.Menu(menu_usuario, tearoff=0)
        menu_usuario.add_cascade (label='Cerrar', command=self.ventana_usuario.destroy)

        # --> imagen
        imagen_usuario = Image.open("./vista/avatar.jpg")  
        imagen_usuario = imagen_usuario.resize((150,150))  #le doy nuevo tamaño (formato tupla: x,y)
        
        self.imagen_usuario = ImageTk.PhotoImage(imagen_usuario)                
        self.label_img_usuario = tk.Label(self.ventana_usuario, image=self.imagen_usuario)   #indico donde se abre el label y le paso la direccion= imagen
        self.label_img_usuario.place( x=415, y=150)  

        # --> etiqueta label
        self.clave_label = tk.Label(self.ventana_usuario)
        self.clave_label.config( text='Contraseña: ', 
                                 font= ('Nunito', 20, 'bold'),
                                 fg='white',
                                 bg=TITULOS)
        self.clave_label.place(x=410, y=350)

        # --> entry de contraseña
        self.clave_usuario = tk.StringVar()
        self.clave_usuario = tk.Entry(self.ventana_usuario)
        self.clave_usuario.config(font=('Nunito', 19),
                                  width=13,
                                  show='*',
                                  textvariable = self.clave_usuario)
        self.clave_usuario.place(x=399, y=400)

        # --> botón
        self.boton_ingresar = tk.Button(self.ventana_usuario)
        self.boton_ingresar.config(text='Iniciar Sesión',
                             font=('Nunito', 14, 'bold'),
                             width=12,
                             fg='white',
                             bg='#805AD5',
                             cursor="hand2") 
        self.boton_ingresar.place(x=418, y=465)  

        self.ventana_usuario.mainloop()      
#-----------------------------------------------
    # --> LOGIN ADMIN
    def ingreso_admin(self):
            if self.clave_admin.get() == "abc123":  # -> clave predefinida
                self.ventana_admin.destroy() # -> Cierra la ventana de login

                # -> Creo  nueva ventana para Admin
                self.panel_admin = tk.Toplevel(self.root)
                self.panel_admin.geometry("1000x600+160+50")     # -> medidas de la ventana
                self.panel_admin.title("Administrador de Centro de Estética")     # -> titulo de la ventana
                Admin(self.panel_admin)      # -> Llamo a la clase Admin
                menu_panel_admin(self.panel_admin)

            else:
               messagebox.showerror("INCORRECTO!", "VERIFIQUE SU CONTRASEÑA")
#-----------------------------------------------
    # --> LOGIN USUARIO

   

