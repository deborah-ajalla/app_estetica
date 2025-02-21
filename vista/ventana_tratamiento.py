import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas import listar_pacientes_por_dni, Tratamiento ,guardar_tratamiento

# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------
class Tratamiento_App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PRIMARY)
        self.place(x=0, y=0, width=1000, height=600) 

        self.dni_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.nombre_t_var = tk.StringVar()

        self.titulo()
        self.label()
        self.entry()
        self.boton_buscar()
        self.boton_limpiar()
        # self.limpiar()
        self.datos_encontrados()
        self.ingresar_tratamiento()
        self.boton_guardar_tratamiento()

    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Gestión de Tratamientos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=283, y=30 )    

    def label(self):
        self.label_dni_buscado = tk.Label(self, text = 'Ingrese el Dni: ')
        self.label_dni_buscado.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14, "bold"))
        self.label_dni_buscado.place(x = 250, y = 112)
    
    def entry(self):
        self.dni_var = tk.StringVar()
        self.dni_buscado = tk.Entry(self, textvariable = self.dni_var)
        self.dni_buscado.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.dni_buscado.place(x = 440, y = 112)
    
    def boton_buscar(self):
        self.boton_buscar = tk.Button (self, text = 'Buscar', command= self.buscar)
        self.boton_buscar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar.place(x = 642, y = 86)
    
    def boton_limpiar(self):
        self.boton_limpiar = tk.Button (self, text = 'Limpiar', command= self.limpiar)
        self.boton_limpiar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_limpiar.place(x = 642, y = 126)

    def buscar(self):
        dni = self.dni_buscado.get().strip()

        if not dni:  # Si el campo está vacío, no mostrar advertencia de inmediato
            messagebox.showwarning("Advertencia", "Por favor, ingrese un DNI...")
            return  
        
        paciente = listar_pacientes_por_dni(dni) # importo de la bd

        if paciente:  # Si el paciente existe, lleno los entrys
            self.dni.set(paciente[2]) 
            self.nombre_var.set(paciente[0])
            self.apellido_var.set(paciente[1])
        else:
            messagebox.showerror("Error", "No se encontró un paciente con ese DNI")
            
    def datos_encontrados(self):
        self.label_paciente = tk.Label(self, text = '——————————  Paciente   ——————————')
        self.label_paciente.config(bg=TITULOS, fg='white', font= ("Nunito", 15))
        self.label_paciente.place(x = 250, y = 195)

        self.label_dni_encontrado = tk.Label(self, text = ' Dni: ')
        self.label_dni_encontrado.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 12))
        self.label_dni_encontrado.place(x = 250, y = 240)

        self.dni = tk.StringVar()
        self.dni_encontrado = tk.Entry (self, textvariable=self.dni)
        self.dni_encontrado.config(width = 15, font = ('Nunito', '12', 'bold'), fg=BOTONES)
        self.dni_encontrado.place(x = 250, y = 262)

        self.label_nombre_encontrado = tk.Label(self, text = ' Nombe: ')
        self.label_nombre_encontrado.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 12))
        self.label_nombre_encontrado.place(x = 433, y = 240)

        self.nombre_var = tk.StringVar()
        self.nombre_encontrado = tk.Entry (self, textvariable=self.nombre_var)
        self.nombre_encontrado.config(width = 15, font = ('Nunito', '12', 'bold'), fg=BOTONES)
        self.nombre_encontrado.place(x = 433, y = 262)

        self.label_apellido_encontrado = tk.Label(self, text = ' Apellido: ')
        self.label_apellido_encontrado.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 12))
        self.label_apellido_encontrado.place(x = 624, y = 240)

        self.apellido_var = tk.StringVar()
        self.apellido_encontrado = tk.Entry (self, textvariable=self.apellido_var)
        self.apellido_encontrado.config(width = 15, font = ('Nunito', '12', 'bold'), fg=BOTONES)
        self.apellido_encontrado.place(x = 624, y = 262)

    def limpiar(self):
        self.dni_var.set("")   # Borra el contenido del Entry 
        self.dni.set("")
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.nombre_t_var.set("")
        self.cuadro_t.delete("1.0", tk.END)

    def ingresar_tratamiento(self):
        self.label_titulo = tk.Label(self, text = 'Tratamiento Realizado: ')
        self.label_titulo.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 12))
        self.label_titulo.place(x = 250, y = 305)

        self.nombre_t_var = tk.StringVar()
        self.nombre_t = tk.Entry(self, textvariable = self.nombre_t_var)
        self.nombre_t.config(width = 36, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.nombre_t.place(x = 440, y = 305)

        self.cuadro_t = tk.Text(self, height=8, width=61, padx= 15, pady= 15, font = ('Arial', '11'), fg=BOTONES)
        self.cuadro_t.place(x = 250, y = 342)
    
    def boton_guardar_tratamiento(self):
        self.boton_guardar_tratamiento = tk.Button (self, text = 'Guardar', command= self.guardar_tratamiento)
        self.boton_guardar_tratamiento.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_guardar_tratamiento.place(x = 452, y = 535)

    def guardar_tratamiento(self):

        nombre_t = self.nombre_t_var.get().strip()  # -> Nombre del tratamiento
        dni = self.dni_var.get().strip()       # -> DNI del paciente
        procedimiento = self.cuadro_t.get("1.0", tk.END).strip()  # -> Procedimiento (texto)               
        
        if not nombre_t or not procedimiento:
            messagebox.showwarning("Advertencia", "El nombre del tratamiento y el procedimiento no pueden estar vacíos.")
            return  # Detener la ejecución si falta algún dato
        
        nuevo_tratamiento = Tratamiento(nombre_t, dni, procedimiento) # -> instancio la clase
    
        guardar_tratamiento(nuevo_tratamiento)

        messagebox.showinfo("Éxito", "Tratamiento guardado correctamente.")
        self.limpiar()
        
    

  

      
