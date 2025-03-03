import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  
from ddbb.consultas import listar_pacientes_por_dni, obtener_turnos_por_fecha
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
        self.bg_image = self.bg_image.resize((1000, 750), Image.Resampling.LANCZOS)  # -> Ajusta al tamaño de la img en el Frame
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # -> Crea un Canvas para colocar la imagen de fondo
        self.canvas = tk.Canvas(self, width=1000, height=700)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.titulo()
        self.fecha()
        self.contenido()
        # self.datos_turno_del_dia ()

        # -> labels de turnos
        self.label_horario_encontrado = tk.Label(self, text= '', font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_encontrado = tk.Label(self, text= "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_encontrado = tk.Label(self, text="",font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_encontrado_2 = tk.Label(self, text= '', font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_encontrado_2 = tk.Label(self, text= "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_encontrado_2 = tk.Label(self, text= "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_encontrado_3 = tk.Label(self, text= '', font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_encontrado_3 = tk.Label(self, text= "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_encontrado_3 = tk.Label(self, text= "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_encontrado_4 = tk.Label(self, text = "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_encontrado_4 = tk.Label(self, text = "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_encontrado_4 = tk.Label(self, text = " ", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_encontrado_5 = tk.Label(self, text = "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_encontrado_5 = tk.Label(self, text = " ", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_encontrado_5 = tk.Label(self, text = "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_horario_encontrado_6 = tk.Label(self, text = "", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_paciente_encontrado_6 = tk.Label(self, text = " ", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
        self.label_profesional_encontrado_6 = tk.Label(self, text = " ", font=("Nunito", 13), bg= '#c7c7c7' ,fg= '#d33393')
    
        # -> labels posicionados
        self.label_horario_encontrado.place(x= 240, y=220)
        self.label_paciente_encontrado.place(x= 270, y= 245)
        self.label_profesional_encontrado.place(x=290, y=270)

        self.label_horario_encontrado_2.place(x= 240, y= 330)
        self.label_paciente_encontrado_2.place(x=270, y= 355)
        self.label_profesional_encontrado_2.place(x= 290, y= 385)

        self.label_horario_encontrado_3.place(x= 240, y= 430)
        self.label_paciente_encontrado_3.place(x=270, y= 455)
        self.label_profesional_encontrado_3.place(x= 290, y= 480)

        self.label_horario_encontrado_4.place(x= 607, y= 220)
        self.label_paciente_encontrado_4.place(x= 639, y= 245)
        self.label_profesional_encontrado_4.place(x= 661, y= 270)

        self.label_horario_encontrado_5.place(x= 607, y= 330)
        self.label_paciente_encontrado_5.place(x= 641, y= 355)
        self.label_profesional_encontrado_5.place(x= 661, y= 385)

        self.label_horario_encontrado_6.place(x= 607, y= 430)
        self.label_paciente_encontrado_6.place(x= 641, y= 455)
        self.label_profesional_encontrado_6.place(x= 661, y= 480)

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

        self.boton_buscar = tk.Button (self, text = ' 🔍', command= self.mostrar_turnos)
        self.boton_buscar.config(width = 8, font = ('Arial', '10', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar.place (x= 570, y= 113)

        self.boton_limpiar = tk.Button (self, text = ' 🧹', command= self.limpiar_turnos)
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
  
    def mostrar_turnos(self):
        fecha = self.fecha_var.get().strip()  # -> Obtiene la fecha del Entry

        if not fecha:  # Si el campo está vacío, no mostrar advertencia de inmediato
            messagebox.showwarning("Advertencia", "Por favor, debe ingresar una fecha...")
            return  
        
        turnos = obtener_turnos_por_fecha(fecha)    # -> Obtiene turnos del paciente
        
        labels_horario = [
            self.label_horario_encontrado, self.label_horario_encontrado_2,
            self.label_horario_encontrado_3, self.label_horario_encontrado_4,
            self.label_horario_encontrado_5, self.label_horario_encontrado_6
        ]
        labels_paciente = [
            self.label_paciente_encontrado, self.label_paciente_encontrado_2,
            self.label_paciente_encontrado_3, self.label_paciente_encontrado_4,
            self.label_paciente_encontrado_5, self.label_paciente_encontrado_6
        ]
        labels_profesional = [
            self.label_profesional_encontrado, self.label_profesional_encontrado_2,
            self.label_profesional_encontrado_3, self.label_profesional_encontrado_4,
            self.label_profesional_encontrado_5, self.label_profesional_encontrado_6
        ]

        # -> Limpia los labels antes de actualizar
        for label in labels_horario + labels_paciente + labels_profesional :  
            label.config(text=" ")

        # -> Asigna valores obtenidos a los Labels
        for i, (horario, nombre, apellido, prof_nombre, prof_apellido) in enumerate (turnos):
            if i < len(labels_horario):  # -> Evita desbordamiento si hay más turnos de los esperados
                labels_horario[i].config(text=horario)
                labels_paciente[i].config(text= f"{nombre} {apellido}")
                labels_profesional[i].config(text=f"{prof_nombre} {prof_apellido}")

        if not turnos:
            messagebox.showinfo("Información", "No hay turnos para esta fecha.")


    def limpiar_turnos(self):
        #  -> Lista de labels a limpiar
        labels = [
            self.label_horario_encontrado, self.label_paciente_encontrado, self.label_profesional_encontrado,
            self.label_horario_encontrado_2, self.label_paciente_encontrado_2, self.label_profesional_encontrado_2,
            self.label_horario_encontrado_3, self.label_paciente_encontrado_3, self.label_profesional_encontrado_3,
            self.label_horario_encontrado_4, self.label_paciente_encontrado_4, self.label_profesional_encontrado_4,
            self.label_horario_encontrado_5, self.label_paciente_encontrado_5, self.label_profesional_encontrado_5,
            self.label_horario_encontrado_6, self.label_paciente_encontrado_6, self.label_profesional_encontrado_6
        ]

        # ->  Recorre los labels y los vacía
        for label in labels:
            label.config(text=" ")
     
        self.fecha_var.set("")   # -> limpia el Entry de fecha