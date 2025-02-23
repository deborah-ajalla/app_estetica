import tkinter as tk
from tkinter import ttk, messagebox

# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------
class Turnos_App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PRIMARY)
        self.place(x=0, y=0, width=1000, height=600) 

        self.titulo()
        self.label()
        self.entry()
        self.boton_buscar_fecha()
        self.boton_reservar()
        self.carga_datos()
        self.boton_guardar_turno()
        self.datos_turno()

    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Gestión de Turnos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=320, y=30 ) 

    def label(self):
        self.label_fecha = tk.Label(self, text = 'Primera Fecha Disponible: ')
        self.label_fecha.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14, "bold"))
        self.label_fecha.place(x = 285, y = 112)
    
    def entry(self):
        self.fecha_var = tk.StringVar()
        self.fecha_disponible = tk.Entry(self, textvariable = self.fecha_var)
        self.fecha_disponible.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.fecha_disponible.place(x = 550, y = 112)

    def boton_buscar_fecha(self):
        self.boton_buscar_fecha = tk.Button (self, text = 'Buscar', command= self.buscar_fecha_turno)
        self.boton_buscar_fecha.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar_fecha.place(x = 345, y = 170)

    def boton_reservar(self):
        self.boton_reservar = tk.Button (self, text = 'Reservar', command= self.reservar_turno)
        self.boton_reservar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_reservar.place(x = 495, y = 170)

    def carga_datos(self):
        self.label_dni_turno = tk.Label(self, text = 'Dni: ')
        self.label_dni_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_dni_turno.place(x = 215, y = 260)

        self.dni_turno_var = tk.StringVar()
        self.dni_turno = tk.Entry(self, textvariable = self.dni_turno_var)
        self.dni_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.dni_turno.place(x = 302, y = 260)

        self.label_nombre_turno = tk.Label(self, text = 'Nombre: ')
        self.label_nombre_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_nombre_turno.place(x = 215, y = 300)

        self.nombre_turno_var = tk.StringVar()
        self.nombre_turno = tk.Entry(self, textvariable = self.nombre_turno_var)
        self.nombre_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.nombre_turno.place(x = 302, y = 300)
        
        self.label_apellido_turno = tk.Label(self, text = 'Apellido: ')
        self.label_apellido_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_apellido_turno.place(x = 215, y = 340)

        self.apellido_turno_var = tk.StringVar()
        self.apellido_turno = tk.Entry(self, textvariable = self.apellido_turno_var)
        self.apellido_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.apellido_turno.place(x = 302, y = 340)

        self.label_cel_turno = tk.Label(self, text = 'Celular: ')
        self.label_cel_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_cel_turno.place(x = 215, y = 380)

        self.cel_turno_var = tk.StringVar()
        self.cel_turno = tk.Entry(self, textvariable = self.cel_turno_var)
        self.cel_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.cel_turno.place(x = 302, y = 380)

        self.label_mail_turno = tk.Label(self, text = 'Mail: ')
        self.label_mail_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_mail_turno.place(x = 215, y = 420)

        self.mail_turno_var = tk.StringVar()
        self.mail_turno = tk.Entry(self, textvariable = self.mail_turno_var)
        self.mail_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.mail_turno.place(x = 302, y = 420)

    def boton_guardar_turno(self):
        self.boton_guardar_turno = tk.Button (self, text = 'Guardar', command= self.buscar_fecha_turno)
        self.boton_guardar_turno.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_guardar_turno.place(x = 270, y = 480)

    def datos_turno(self):
        self.cuadro_turno= tk.Text(self, height=9, width=30, padx= 15, pady= 23, font = ('Arial', '11'), fg=BOTONES)
        self.cuadro_turno.place(x = 490, y = 260)



    def buscar_fecha_turno(self):
        pass

    def reservar_turno(self):
        pass
    