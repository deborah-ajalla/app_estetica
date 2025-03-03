import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas import Profesional, crear_tabla, guardar_profesional, editar_profesional, listar_profesionales, borrar_profesional
#--------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------
class Profesionales(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PRIMARY)
        self.id_profesional = None
        self.place(x=0, y=0, width=1000, height=600) 

        self.titulo()
        self.carga_datos()

    def titulo(self):
        self.etiqueta_titulo = tk.Label(self, text= "✦ Profesionales ✦ ", font=("Nunito", 24,  "bold"), fg=TITULOS, bg=PRIMARY)
        self.etiqueta_titulo.place(x=350, y=30 )
#-----------------------------------------------  
    def carga_datos(self):
        # -> Labels
        self.nombre_prof = tk.Label(self, text = 'Nombre: ')
        self.nombre_prof.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.nombre_prof.place(x = 100, y = 110)

        self.apellido_prof = tk.Label(self, text = 'Apellido: ')
        self.apellido_prof.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.apellido_prof.place(x = 100, y = 150)

        self.dni_prof = tk.Label(self, text = 'Dni: ')
        self.dni_prof.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.dni_prof.place(x = 100, y = 190)

        self.cel_prof = tk.Label(self, text = 'Celular: ')
        self.cel_prof.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.cel_prof.place(x = 520, y = 110)

        self.mail_prof = tk.Label(self, text = 'Email : ')
        self.mail_prof.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.mail_prof.place(x = 520, y = 150)

        self.especialidad_prof = tk.Label(self, text = 'Email : ')
        self.especialidad_prof.config(bg=PRIMARY,fg=TITULOS,font= ("Nunito", 15, "bold"))
        self.especialidad_prof.place(x = 520, y = 190)

        # -> Entrys
        self.nombre_var = tk.StringVar()
        self.entry_nombre_prof = tk.Entry(self, textvariable = self.nombre_var)
        self.entry_nombre_prof.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_nombre_prof.place(x = 200, y = 110)

        self.apellido_var = tk.StringVar()
        self.entry_apellido_prof = tk.Entry(self, textvariable = self.apellido_var)
        self.entry_apellido_prof.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_apellido_prof.place(x = 200, y = 150)

        self.dni_var = tk.StringVar()
        self.entry_dni_prof = tk.Entry(self, textvariable = self.dni_var)
        self.entry_dni_prof.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_dni_prof.place(x = 200, y = 190)

        self.cel_var = tk.StringVar()
        self.entry_cel_prof = tk.Entry(self, textvariable = self.cel_var)
        self.entry_cel_prof.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_cel_prof.place(x = 620, y = 110)

        self.mail_var = tk.StringVar()
        self.entry_mail_prof = tk.Entry(self, textvariable = self.mail_var)
        self.entry_mail_prof.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_mail_prof.place(x = 620, y = 150)

        self.especialidad_var = tk.StringVar()
        self.entry_especialidad_prof = tk.Entry(self, textvariable=self.especialidad_var)
        self.entry_especialidad_prof.config(width = 28, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entry_especialidad_prof.place(x = 620, y = 190)
#-----------------------------------------------
    def botones(self):
        self.boton_nuevo = tk.Button (self, text = 'Nuevo', command = self.habilitar_campos)
        self.boton_nuevo.config(width = 18, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_nuevo.place(x = 130, y = 260)

        self.boton_guardar = tk.Button (self, text = 'Guardar', command = self.guardar_campos)
        self.boton_guardar.config(width = 18, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES, cursor='hand2')
        self.boton_guardar.place(x = 410, y = 260)

        self.boton_cancelar = tk.Button (self, text = 'Cancelar', command = self.bloquear_campos)
        self.boton_cancelar.config(width = 18, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES, cursor='hand2')
        self.boton_cancelar.place(x = 690, y = 260)
#-----------------------------------------------   
    def guardar_campos(self):
        profesional = Profesional(    # -> se instancia la clase
            self.nombre_var.get(),
            self.apellido_var.get(),
            self.dni_var.get(),
            self.cel_var.get(),
            self.mail_var.get(),
            self.especialidad_var.get()
        )

        if self.id_profesional == None:
            guardar_profesional(profesional)
        else:
            editar_profesional(profesional,int(self.id_profesional))
        
        self.bloquear_campos()
        self.mostrar_tabla()    
#-----------------------------------------------   
    def habilitar_campos(self):
        self.entry_nombre_prof.config (state= 'normal')
        self.entry_apellido_prof.config (state='normal')
        self.entry_dni_prof.config (state='normal')
        self.entry_cel_prof.config (state='normal')
        self.entry_mail_prof.config (state='normal')
        self.entry_especialidad_prof.config (state='normal')
        self.boton_guardar.config (state='normal')
        self.boton_cancelar.config (state='normal')
        self.boton_nuevo.config (state='disabled')

        self.entry_nombre_prof.focus_set()      # -> Coloca el cursor en el Entry de nombre
#-----------------------------------------------
    def bloquear_campos(self):
        self.entry_nombre_prof.config (state='disabled')
        self.entry_apellido_prof.config (state='disabled')
        self.entry_dni_prof.config (state='disabled')
        self.entry_cel_prof.config (state='disabled')
        self.entry_mail_prof.config (state='disabled')
        self.entry_especialidad_prof.config (state='disabled')
        self.boton_guardar.config (state='disabled')
        self.boton_cancelar.config (state='disabled')
        self.boton_nuevo.config (state='normal')
        self.nombre_var.set('')
        self.apellido_var.set('')
        self.dni_var.set('')
        self.cel_var.set('')
        self.mail_var.set('')
        self.especialidad_var.set ('')
        self.id_profesional = None
#-----------------------------------------------
    def mostrar_tabla(self):
        self.lista_pro = listar_profesionales()  # --> me trae el listado que capturo con el fetchall
        self.lista_pro.reverse()             # --> invierte el orden sino aparecen en orden de agregado

        self.tabla = ttk.Treeview(self, column = ('Nombre', 'Apellido','Dni', 'Celular', 'Mail', 'Especialidad'))
        self.tabla.place(x =20, y = 310, width=960, height=220) 

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'Nombre')
        self.tabla.heading('#2', text = 'Apellido' )
        self.tabla.heading('#3', text = 'Dni')
        self.tabla.heading('#4', text = 'Celular')
        self.tabla.heading('#5', text = 'Mail')
        self.tabla.heading('#6', text = 'Especialidad')

        self.tabla.column ('#0', anchor = 'center', width = 20)
        self.tabla.column ('#1', anchor = 'center', width = 100)
        self.tabla.column ('#2', anchor = 'center', width = 100)
        self.tabla.column ('#3', anchor = 'center', width = 100)
        self.tabla.column ('#4', anchor = 'center', width = 100)
        self.tabla.column ('#5', anchor = 'center', width = 100)
        self.tabla.column ('#6', anchor = 'center', width = 100)

        # --> iterar lista de pacientes
        for p in self.lista_pro:                      
            self.tabla.insert('',0,text=p[0],   #  --> el [0] es el id
                               values = (p[1],p[2],p[3],p[4],p[5],p[6])) # --> inserta los valores en cada campo

        # --> Botones
        self.boton_modificar = tk.Button (self, text = 'Modificar', command=self.editar_registros)
        self.boton_modificar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_modificar.place(x = 220, y = 550)

        self.boton_eliminar = tk.Button (self, text = 'Eliminar', command = self.eliminar_registros)
        self.boton_eliminar.config(width = 18, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_eliminar.place(x = 550, y = 550)
#-----------------------------------------------
    def editar_registros(self):
        try:
             self.id_profesional = self.tabla.item(self.tabla.selection())['text']

             self.nombre_profesional = self.tabla.item (self.tabla.selection())['values'][0]
             self.apellido_profesional = self.tabla.item(self.tabla.selection())['values'][1]
             self.dni_profesional = self.tabla.item(self.tabla.selection())['values'][2]
             self.cel_profesional = self.tabla.item(self.tabla.selection())['values'][3]
             self.mail_profesional = self.tabla.item(self.tabla.selection())['values'][4]
             self.especialidad_profesional = self.tabla.item(self.tabla.selection())['values'][5]

             self.habilitar_campos()

             self.nombre.set(self.nombre_profesional)
             self.apellido.set(self.apellido_profesional)
             self.dni.set (self.dni_profesional)
             self.cel.set(self.cel_profesional)
             self.mail.set(self.mail_profesional)
             self.especialidad.set (self.especialidad_profesional)

        except:
             pass  
#-----------------------------------------------
    def eliminar_registros(self):
        self.id_profesional = self.tabla.item(self.tabla.selection())['text']

        borrar_profesional(int(self.id_profesional))

        self.mostrar_tabla()


