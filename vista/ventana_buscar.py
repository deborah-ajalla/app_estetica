import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas import listar_pacientes_por_dni
#----------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#----------------------------------
class Buscar (tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=1050, height=600, bg=TITULOS)
        self.root = root
        self.id_paciente = None
        self.pack()
       
        self.titulo()
        self.label()
        self.entry()
        self.boton_buscar()
        self.boton_limpiar()
        self.limpiar()
      
    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Búsqueda de Pacientes ✦ ", font=("Nunito", 22, "bold"), fg='white', bg=TITULOS)
        self.titulo.place(x=240, y=35)
    
    def label(self):
        self.label_dni_buscado = tk.Label(self, text = 'Ingrese el Dni: ')
        self.label_dni_buscado.config(bg=TITULOS, fg='white', font= ("Nunito", 14, "bold"))
        self.label_dni_buscado.place(x = 300, y = 100)
    
    def entry(self):
        self.dni_var = tk.StringVar()
        self.dni_buscado = tk.Entry(self, textvariable = self.dni_var)
        self.dni_buscado.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.dni_buscado.place(x = 448, y = 100)
    
    def boton_buscar(self):
        self.boton_buscar = tk.Button (self, text = 'Buscar', command= self.buscar_paciente)
        self.boton_buscar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar.place(x = 315, y = 160)
    
    def boton_limpiar(self):
        self.boton_limpiar = tk.Button (self, text = 'Limpiar', command= self.limpiar)
        self.boton_limpiar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_limpiar.place(x = 452, y = 160)
      
    
    def buscar_paciente(self):
        dni = self.dni_buscado.get().strip()

        if not dni:  # Si el campo está vacío, no mostrar advertencia de inmediato
            messagebox.showwarning("Advertencia", "Por favor, ingrese un DNI...")
            return  

        paciente = listar_pacientes_por_dni(dni)

        if not hasattr(self, 'cuadro_texto'): # si no hay cuadro de texto -> lo crea
            self.cuadro_texto = tk.Text(self, height=10, width=50, padx= 10, pady= 15, font = ('Arial', '11', 'bold'), fg=BOTONES)
            self.cuadro_texto.place(x = 238, y = 215)

        self.cuadro_texto.delete("1.0", tk.END)

        if paciente:
            self.cuadro_texto.insert(tk.END, f"- Nombre: {paciente[0]}\n- Apellido: {paciente[1]}\n- DNI: {paciente[2]}\n- Celular: {paciente[3]}\n- Email: {paciente[4]}".title())

            
            if not hasattr(self, 'boton_salir'):  # Si el botón de salir aún no existe -> lo crea
                self.boton_salir = tk.Button (self, text = 'Salir', command= self.salir)
                self.boton_salir.config(width = 11, font = ('Arial', '10', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
                self.boton_salir.place(x = 403, y = 460)

        else:
            messagebox.showwarning("ADVERTENCIA!", "EL DNI INGRESADO NO ESTÁ REGISTRADO...")
            self.cuadro_texto.insert(tk.END, "Debe ingresar un DNI para comenzar la búsqueda...")
    
    def limpiar(self):
        self.dni_var.set("")   # Borra el contenido del Entry
        if hasattr(self, 'cuadro_texto'):  # Si el cuadro de texto existe, limpiarlo
            self.cuadro_texto.delete("1.0", tk.END)
    
    def salir(self):
        self.root.destroy()  # Cierra la ventana


        

    