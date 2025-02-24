import tkinter as tk
import datetime
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
      
        self.campos_cargados = False    # Inicialmente los campos de datos están ocultos

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

        self.label_nombre_turno = tk.Label(self, text = 'Nombre: ')
        self.label_nombre_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_nombre_turno.place(x = 215, y = 260)

        self.nombre_turno_var = tk.StringVar()
        self.nombre_turno = tk.Entry(self, textvariable = self.nombre_turno_var)
        self.nombre_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        # self.nombre_turno.place(x = 302, y = 260)
        
        self.label_apellido_turno = tk.Label(self, text = 'Apellido: ')
        self.label_apellido_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        # self.label_apellido_turno.place(x = 215, y = 300)

        self.apellido_turno_var = tk.StringVar()
        self.apellido_turno = tk.Entry(self, textvariable = self.apellido_turno_var)
        self.apellido_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        # self.apellido_turno.place(x = 302, y = 300)

        self.label_dni_turno = tk.Label(self, text = 'Dni: ')
        self.label_dni_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        # self.label_dni_turno.place(x = 215, y = 340)

        self.dni_turno_var = tk.StringVar()
        self.dni_turno = tk.Entry(self, textvariable = self.dni_turno_var)
        self.dni_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        # self.dni_turno.place(x = 302, y = 340)

        self.label_cel_turno = tk.Label(self, text = 'Celular: ')
        self.label_cel_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        # self.label_cel_turno.place(x = 215, y = 380)

        self.cel_turno_var = tk.StringVar()
        self.cel_turno = tk.Entry(self, textvariable = self.cel_turno_var)
        self.cel_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        # self.cel_turno.place(x = 302, y = 380)

        self.label_mail_turno = tk.Label(self, text = 'Mail: ')
        self.label_mail_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        # self.label_mail_turno.place(x = 215, y = 420)

        self.mail_turno_var = tk.StringVar()
        self.mail_turno = tk.Entry(self, textvariable = self.mail_turno_var)
        self.mail_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        # self.mail_turno.place(x = 302, y = 420)

        self.cuadro_turno= tk.Text(self, height=9, width=30, padx= 15, pady= 23, font = ('Arial', '11'), fg=BOTONES)
        # self.cuadro_turno.place(x = 490, y = 260)

        self.boton_guardar_turno = tk.Button (self, text = 'Guardar', command=self.guardar_turno)
        self.boton_guardar_turno.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_imprimir = tk.Button (self, text = 'Imprimir')
        self.boton_imprimir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_qr = tk.Button (self, text = 'QR')
        self.boton_qr.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

    
    def mostrar_campos_datos(self):  # -> muestro los campos despues de click en reservar
        self.label_nombre_turno.place(x=215, y=260)
        self.nombre_turno.place(x=302, y=260)  # entry

        self.label_apellido_turno.place(x=215, y=300)
        self.apellido_turno.place(x=302, y=300) # entry

        self.label_dni_turno.place(x=215, y=340)
        self.dni_turno.place(x=302, y=340) # entry

        self.label_cel_turno.place(x=215, y=380)
        self.cel_turno.place(x=302, y=380) # entry

        self.label_mail_turno.place(x=215, y=420)
        self.mail_turno.place(x=302, y=420) # entry

        self.cuadro_turno.place(x=490, y=260)  # cuadro de texto

        self.boton_guardar_turno.place(x = 270, y = 480) # botón

        self.boton_imprimir.place(x = 505, y = 480)  # botón

        self.boton_qr.place(x = 630, y = 480)   # botón


    # def boton_guardar_turno(self):
    #     self.boton_guardar_turno = tk.Button (self, text = 'Guardar')
    #     self.boton_guardar_turno.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
    #     self.boton_guardar_turno.place(x = 270, y = 480)

    # def datos_turno(self):
    #     self.cuadro_turno= tk.Text(self, height=9, width=30, padx= 15, pady= 23, font = ('Arial', '11'), fg=BOTONES)
    #     self.cuadro_turno.place(x = 490, y = 260)

    # def boton_imprimir(self):
    #     self.boton_imprimir = tk.Button (self, text = 'Imprimir')
    #     self.boton_imprimir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
    #     self.boton_imprimir.place(x = 505, y = 480)

    # def boton_qr(self):
    #     self.boton_qr = tk.Button (self, text = 'QR')
    #     self.boton_qr.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
    #     self.boton_qr.place(x = 630, y = 480)


    def buscar_fecha_turno(self):       # -> Habilitar el label de fecha y mostrar una fecha ficticia
        fecha_actual = datetime.date.today()     # -> obtiene la fecha actual
        fecha_disponible = fecha_actual + datetime.timedelta(days=3)  # -> Ej: Primera fecha disponible en 3 días
        self.fecha_var.set(fecha_disponible.strftime("%d/%m/%Y"))     # -> inserta en el 

    def reservar_turno(self):   # -> Capturar los datos ingresados     
        if not self.campos_cargados:
            self.carga_datos()  # Crea los campos solo una vez
            self.mostrar_campos_datos()
            self.campos_cargados = True

    def guardar_turno(self):
        nombre = self.nombre_turno_var.get()
        apellido = self.apellido_turno_var.get()
        dni = self.dni_turno_var.get()
        celular = self.cel_turno_var.get()
        mail = self.mail_turno_var.get()
        fecha = self.fecha_var.get()
       
        if not (nombre and apellido and dni and celular and mail and fecha): # -> Valida que todos los datos estén completos
            messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos antes de reservar.")
            return

        # Muestro los datos en el cuadro de texto
        self.cuadro_turno.delete(1.0, tk.END)  # Limpiar el cuadro
        reserva_texto = f"~~~ Reserva Confirmada ~~~\n\n -   Fecha: {fecha}\n -   Nombre: {(nombre).title()} {(apellido).title()}\n -   DNI: {dni}\n -   Celular: {celular}\n -   Email: {mail} \n~~~~~~~~~~~~~~~~~~~~~~"
        self.cuadro_turno.insert(tk.END, reserva_texto)

        messagebox.showinfo("Reserva Confirmada", "Su turno ha sido reservado correctamente.")
    
    def imprimir (self):
        pass

    def qr (self):
        pass