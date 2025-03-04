import tkinter as tk
from tkinter import ttk, messagebox
#--------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"
#--------------------------------
class Productos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=PRIMARY)
        self.place(x=0, y=0, width=1000, height=600) 

        self.titulo()
        self.tabla()
#-----------------------------------------------
    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Productos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=380, y=30 )    
#-----------------------------------------------
    def tabla(self):
        self.tabla = ttk.Treeview(self, column = ('Codigo','Nombre', 'Precio','Cantidad'))
        self.tabla.place(x =90, y = 100, width=800, height=300) 

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'Codigo')
        self.tabla.heading('#2', text = 'Nombre')
        self.tabla.heading('#3', text = 'Precio' )
        self.tabla.heading('#4', text = 'Cantidad')

        self.tabla.column ('#0', anchor = 'center', width = 20)
        self.tabla.column ('#1', anchor = 'center', width = 30)
        self.tabla.column ('#2', anchor = 'center', width = 120)
        self.tabla.column ('#3', anchor = 'center', width = 70)
        self.tabla.column ('#4', anchor = 'center', width = 70)

        # --> Botones
        self.boton_ver = tk.Button (self, text = 'Ver Detalle')
        self.boton_ver.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_ver.place(x = 90, y = 440)

        self.boton_agregar = tk.Button (self, text = 'Agregar', command= self.agregar)
        self.boton_agregar.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_agregar.place(x = 300, y = 440)

        self.boton_modificar = tk.Button (self, text = 'Modificar')
        self.boton_modificar.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_modificar.place(x = 505, y = 440)

        self.boton_eliminar = tk.Button (self, text = 'Eliminar')
        self.boton_eliminar.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_eliminar.place(x = 720, y = 440)

        self.boton_vender = tk.Button (self, text = 'Vender')
        self.boton_vender.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_vender.place(x = 400, y = 510)
#-----------------------------------------------
    def agregar(self):
        # -> Creo ventana nueva para agregar un producto
        ventana_agregar = tk.Toplevel(self)
        ventana_agregar.title("Agregar Producto")
        ventana_agregar.config(bg=TITULOS)
        ventana_agregar.geometry("500x300+420+130")
        ventana_agregar.resizable(0,0)

        # ->  Creo etiquetas y entradas para los campos del producto
        etiqueta_codigo = tk.Label(ventana_agregar, text="Código:")
        etiqueta_codigo.config(bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        etiqueta_codigo.place(x=100, y=40 )    
        entrada_codigo = tk.Entry(ventana_agregar)
        entrada_codigo.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        entrada_codigo.place(x=210, y=45 )   

        etiqueta_nombre = tk.Label(ventana_agregar, text="Nombre:")
        etiqueta_nombre.config (bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        etiqueta_nombre.place(x=100, y=75 )  
        entrada_nombre = tk.Entry(ventana_agregar)
        entrada_nombre.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        entrada_nombre.place(x=210, y=80 )  

        etiqueta_precio = tk.Label(ventana_agregar, text="Precio:")
        etiqueta_precio.config(bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        etiqueta_precio.place(x=100, y=110 )  
        entrada_precio = tk.Entry(ventana_agregar)
        entrada_precio.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        entrada_precio.place(x=210, y=115)  

        etiqueta_stock = tk.Label(ventana_agregar, text="Cantidad:")
        etiqueta_stock.config (bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        etiqueta_stock.place(x=100, y=145 )  
        entrada_stock = tk.Entry(ventana_agregar)
        entrada_stock.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        entrada_stock.place(x=210, y=150 )  
        
        # Botón para agregar el producto
        boton_agregar = tk.Button(ventana_agregar, text="Agregar", command=lambda: self.agregar_producto(ventana_agregar, entrada_codigo.get(), entrada_nombre.get(), entrada_precio.get(), entrada_stock.get()))
        boton_agregar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_agregar.place(x=90, y=210 )  

        # Botón para cancelar la operación
        boton_cancelar = tk.Button(ventana_agregar, text="Cancelar", command=ventana_agregar.destroy)
        boton_cancelar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_cancelar.place(x=260, y=210 )  
#-----------------------------------------------