import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas import listar_pacientes_por_dni
#----------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"

class Ver_tratamientos (tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=1050, height=600, bg=TITULOS)
        self.root = root
        self.id_paciente = None
        self.pack()

        self.titulo()
        self.label()
        self.entry()
        self.boton_buscar_tto()
        self.boton_limpiar_tto()
        self.datos_encontrados()


    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Búsqueda de Tratamientos ✦ ", font=("Nunito", 22, "bold"), fg='white', bg=TITULOS)
        self.titulo.place(x=220, y=35)
    
    def label(self):
        self.label_dni_buscado = tk.Label(self, text = 'Ingrese el Dni: ')
        self.label_dni_buscado.config(bg=TITULOS, fg='white', font= ("Nunito", 14, "bold"))
        self.label_dni_buscado.place(x = 300, y = 100)
    
    def entry(self):
        self.dni_var = tk.StringVar()
        self.dni_buscado = tk.Entry(self, textvariable = self.dni_var)
        self.dni_buscado.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.dni_buscado.place(x = 448, y = 100)

    def boton_buscar_tto(self):
        self.boton_buscar_tto = tk.Button (self, text = 'Buscar', command= self.buscar_tto)
        self.boton_buscar_tto.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar_tto.place(x = 315, y = 160)
    
    def boton_limpiar_tto(self):
        self.boton_limpiar_tto = tk.Button (self, text = 'Limpiar', command= self.limpiar_tto)
        self.boton_limpiar_tto.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_limpiar_tto.place(x = 452, y = 160)

    def datos_encontrados(self):
        self.label_paciente = tk.Label(self, text = '———  Paciente  ———')
        self.label_paciente.config(bg=TITULOS, fg='white', font= ("Nunito", 15))
        self.label_paciente.place(x = 120, y = 215)

        self.label_nombre_encontrado = tk.Label(self, text = ' Nombre: ')
        self.label_nombre_encontrado.config(bg=TITULOS, fg='white', font= ("Nunito", 12))
        self.label_nombre_encontrado.place(x = 150, y = 250)

        self.nombre_var = tk.StringVar()
        self.nombre_encontrado = tk.Entry (self, textvariable=self.nombre_var)
        self.nombre_encontrado.config(width = 15, font = ('Nunito', '12', 'bold'), fg=BOTONES)
        self.nombre_encontrado.place(x = 150, y = 280)

        self.label_apellido_encontrado = tk.Label(self, text = ' Apellido: ')
        self.label_apellido_encontrado.config(bg=TITULOS, fg= 'white', font= ("Nunito", 12))
        self.label_apellido_encontrado.place(x = 150, y = 320)

        self.apellido_var = tk.StringVar()
        self.apellido_encontrado = tk.Entry (self, textvariable=self.apellido_var)
        self.apellido_encontrado.config(width = 15, font = ('Nunito', '12', 'bold'), fg=BOTONES)
        self.apellido_encontrado.place(x = 150, y = 350)

        self.label_tto = tk.Label(self, text = '——————  Tratamientos  ——————')
        self.label_tto.config(bg=TITULOS, fg='white', font= ("Nunito", 15))
        self.label_tto.place(x = 400, y = 215)

        self.cuadro_tto = tk.Text(self, height=8, width=45, padx= 10, pady= 15, font = ('Arial', '11', 'bold'), fg=BOTONES)
        self.cuadro_tto.place(x = 400, y = 250)

        self.boton_salir = tk.Button (self, text = 'Salir', command= self.salir)
        self.boton_salir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_salir.place(x = 390, y = 450)



    def buscar_tto(self):
        pass

    def limpiar_tto(self):
        pass

    def salir(self):
        self.root.destroy()  # Cierra la ventana
