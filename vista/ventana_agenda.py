import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  
#--------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------
class Agenda(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=TITULOS)
        self.place(x=0, y=0, width=1000, height=600) 

        # -> Cargo la imagen de fondo
        self.bg_image = Image.open("./vista/agenda.JPG")  
        self.bg_image = self.bg_image.resize((1000, 750), Image.Resampling.LANCZOS)  # -> Ajusta al tamaño del Frame
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # -> Crea un Canvas para colocar la imagen de fondo
        self.canvas = tk.Canvas(self, width=1000, height=700)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.titulo()
        self.fecha()
        self.contenido()

    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Agenda ✦ ", font=("Nunito", 22, "bold"), bg='#d33393', fg="white")
        self.titulo.place(x=400, y=30 ) 

    def fecha(self):
        self.label_fecha = tk.Label(self, text= "Fecha: ", font=("Nunito", 16, "bold"), bg='#b8769c', fg= 'white')
        self.label_fecha.place(x= 330, y= 110)

        self.fecha_var = tk.StringVar()
        self.fecha_turno = tk.Entry(self, textvariable = self.fecha_var)
        self.fecha_turno.config(width = 13, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.fecha_turno.place(x = 420, y = 115)

        self.boton_buscar = tk.Button (self, text = ' 🔍')
        self.boton_buscar.config(width = 8, font = ('Arial', '10', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar.place (x= 570, y= 113)

        self.boton_limpiar = tk.Button (self, text = ' 🧹')
        self.boton_limpiar.config(width = 8, font = ('Arial', '10', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_limpiar.place (x= 660, y= 113)

    def contenido(self):
        self.label_horario = tk.Label(self, text = " Hora: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario.place(x= 180, y= 220)

        self.label_paciente = tk.Label(self, text = " Paciente: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente.place(x= 180, y= 245)

        self.label_profesional = tk.Label(self, text = " Profesional: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional.place(x= 180, y= 270)

        self.label_divisor = tk.Label(self, text = " _____________________ ", font=("Nunito", 12, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_divisor.place(x= 180, y= 290)

        self.label_horario_2 = tk.Label(self, text = " Hora: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_2.place(x= 180, y= 330)

        self.label_paciente_2 = tk.Label(self, text = " Paciente: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_2.place(x= 180, y= 355)

        self.label_profesional_2 = tk.Label(self, text = " Profesional: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_2.place(x= 180, y= 375)

        self.label_divisor_2 = tk.Label(self, text = " _____________________ ", font=("Nunito", 12, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_divisor_2.place(x= 180, y= 400)

        self.label_horario_3 = tk.Label(self, text = " Hora: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_3.place(x= 180, y= 430)

        self.label_paciente_3 = tk.Label(self, text = " Paciente: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_3.place(x= 180, y= 455)

        self.label_profesional_3 = tk.Label(self, text = " Profesional: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_3.place(x= 180, y= 480)

        self.label_horario_4 = tk.Label(self, text = " Hora: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_4.place(x= 552, y= 220)

        self.label_paciente_4 = tk.Label(self, text = " Paciente: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_4.place(x= 552, y= 245)

        self.label_profesional_4 = tk.Label(self, text = " Profesional: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_4.place(x= 552, y= 270)

        self.label_divisor_3 = tk.Label(self, text = " _____________________ ", font=("Nunito", 12, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_divisor_3.place(x= 552, y= 290)

        self.label_horario_5 = tk.Label(self, text = " Hora: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_5.place(x= 554, y= 330)

        self.label_paciente_5 = tk.Label(self, text = " Paciente: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_5.place(x= 554, y= 355)

        self.label_profesional_5 = tk.Label(self, text = " Profesional: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_5.place(x= 554, y= 375)

        self.label_divisor_5 = tk.Label(self, text = " _____________________ ", font=("Nunito", 12, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_divisor_5.place(x= 554, y= 400)

        self.label_horario_6 = tk.Label(self, text = " Hora: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_6.place(x= 556, y= 430)

        self.label_paciente_6 = tk.Label(self, text = " Paciente: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_6.place(x= 556, y= 455)

        self.label_profesional_6 = tk.Label(self, text = " Profesional: ", font=("Nunito", 13, "bold"), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_6.place(x= 556, y= 480)

      