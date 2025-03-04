import tkinter as tk
from tkinter import ttk, messagebox
from ddbb.consultas import Producto, guardar_producto, listar_productos, editar_producto_en_bd, borrar_producto
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
       
        self.id_producto = None
        self.place(x=0, y=0, width=1000, height=600) 

        self.titulo()
        self.mostrar_tabla()
#-----------------------------------------------
    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Productos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=380, y=30 )    
#-----------------------------------------------
    def mostrar_tabla(self):
        self.lista_prod = listar_productos()  # --> me trae el listado que capturo con el fetchall
        self.lista_prod.reverse()             # --> invierte el orden sino aparecen en orden de agregado

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

        # --> iterar lista de productos
        for p in self.lista_prod:                      
            self.tabla.insert('',0,text=p[0],   #  --> el [0] es el id
                               values = (p[1],p[2],p[3],p[4])) # --> inserta los valores en cada campo

        self.boton_agregar = tk.Button (self, text = 'Agregar', command= self.agregar)
        self.boton_agregar.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_agregar.place(x = 195, y = 440)

        self.boton_modificar = tk.Button (self, text = 'Modificar', command= self.modificar)
        self.boton_modificar.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_modificar.place(x = 400, y = 440)

        self.boton_eliminar = tk.Button (self, text = 'Eliminar', command= self.eliminar)
        self.boton_eliminar.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_eliminar.place(x = 615, y = 440)

        self.boton_vender = tk.Button (self, text = 'Vender')
        self.boton_vender.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_vender.place(x = 400, y = 510)
#-----------------------------------------------
    def agregar(self):
        # -> Creo ventana nueva para agregar un producto
        self.ventana_agregar = tk.Toplevel(self)
        self.ventana_agregar.title("Agregar Producto")
        self.ventana_agregar.config(bg=TITULOS)
        self.ventana_agregar.geometry("500x300+420+130")
        self.ventana_agregar.resizable(0,0)

        # ->  Creo etiquetas y entradas para los campos del producto
        self.etiqueta_codigo = tk.Label(self.ventana_agregar, text="Código:")
        self.etiqueta_codigo.config(bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self.etiqueta_codigo.place(x=100, y=40 )    
        self. entrada_codigo = tk.Entry(self.ventana_agregar)
        self.entrada_codigo.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entrada_codigo.place(x=210, y=45 )   

        self. etiqueta_nombre = tk.Label(self.ventana_agregar, text="Nombre:")
        self. etiqueta_nombre.config (bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self. etiqueta_nombre.place(x=100, y=75 )  
        self. entrada_nombre = tk.Entry(self.ventana_agregar)
        self. entrada_nombre.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self. entrada_nombre.place(x=210, y=80 )  

        self. etiqueta_precio = tk.Label(self.ventana_agregar, text="Precio:")
        self. etiqueta_precio.config(bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self. etiqueta_precio.place(x=100, y=110 )  
        self. entrada_precio = tk.Entry(self.ventana_agregar)
        self. entrada_precio.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self. entrada_precio.place(x=210, y=115)  

        self. etiqueta_stock = tk.Label(self.ventana_agregar, text="Cantidad:")
        self. etiqueta_stock.config (bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self. etiqueta_stock.place(x=100, y=145 )  
        self. entrada_stock = tk.Entry(self.ventana_agregar)
        self. entrada_stock.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self. entrada_stock.place(x=210, y=150 )  
        
        # -> Botón para agregar el producto
        boton_agregar = tk.Button(self.ventana_agregar, text="Agregar", command= self.agregar_producto)
        boton_agregar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_agregar.place(x=90, y=210 )  

        # -> Botón para cancelar la operación
        boton_cancelar = tk.Button(self.ventana_agregar, text="Cancelar", command= self.ventana_agregar.destroy)
        boton_cancelar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_cancelar.place(x=260, y=210 )  
 #-----------------------------------------------   
    def agregar_producto(self):        
        producto = Producto(    # -> se instancia la clase
            self.entrada_codigo.get(),
            self.entrada_nombre.get(),
            self.entrada_precio.get(),
            self.entrada_stock.get()
        )

        if self.id_producto == None:
            guardar_producto(producto)  # -> Guarda en la base de datos
        else:
            editar_producto_en_bd (producto,int(self.id_producto))

        self.mostrar_tabla()

        # -> Cierra la ventana de agregar
        self.ventana_agregar.destroy()      
#-----------------------------------------------
    def modificar(self):
        # -> Obtengo el item seleccionado
        self.item_seleccionado = self.tabla.selection()

        if not self.item_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para editar")
            return

        # > Obtengo los valores del item seleccionado
        valores = self.tabla.item(self.item_seleccionado, "values")

        # -> Si el producto tiene valores, abrir ventana para editar
        if valores:
            self.editar_producto(valores)
#-----------------------------------------------
    def editar_producto(self, valores):       

         # -> Creo ventana nueva para modificar un producto
        self.ventana_editar = tk.Toplevel(self)
        self.ventana_editar.title("Modificar Producto")
        self.ventana_editar.config(bg=TITULOS)
        self.ventana_editar.geometry("500x300+420+130")
        self.ventana_editar.resizable(0,0)

        # -> Extraigo valores del producto seleccionado
        codigo, nombre, precio, cantidad = valores

        # ->  Creo etiquetas y entradas para los campos del producto
        self.etiqueta_codigo = tk.Label(self.ventana_editar, text="Código:")
        self.etiqueta_codigo.config(bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self.etiqueta_codigo.place(x=100, y=40 )    
        self. entrada_codigo = tk.Entry(self.ventana_editar)
        self.entrada_codigo.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.entrada_codigo.place(x=210, y=45 )   
        self.entrada_codigo.insert(0, codigo)  # Insertar valor obtenido

        self. etiqueta_nombre = tk.Label(self.ventana_editar, text="Nombre:")
        self. etiqueta_nombre.config (bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self. etiqueta_nombre.place(x=100, y=75 )  
        self. entrada_nombre = tk.Entry(self.ventana_editar)
        self. entrada_nombre.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self. entrada_nombre.place(x=210, y=80 )  
        self.entrada_nombre.insert(0, nombre) # Insertar valor obtenido

        self. etiqueta_precio = tk.Label(self.ventana_editar, text="Precio:")
        self. etiqueta_precio.config(bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self. etiqueta_precio.place(x=100, y=110 )  
        self. entrada_precio = tk.Entry(self.ventana_editar)
        self. entrada_precio.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self. entrada_precio.place(x=210, y=115)  
        self.entrada_precio.insert(0, precio) # Insertar valor obtenido

        self. etiqueta_cantidad = tk.Label(self.ventana_editar, text="Cantidad:")
        self. etiqueta_cantidad.config (bg=TITULOS,fg='white',font= ("Nunito", 15, "bold"))
        self. etiqueta_cantidad.place(x=100, y=145 )  
        self. entrada_cantidad = tk.Entry(self.ventana_editar)
        self. entrada_cantidad.config(width = 20, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self. entrada_cantidad.place(x=210, y=150 )  
        self. entrada_cantidad.insert(0, cantidad)  # Insertar valor obtenido
        
        # -> Botón para agregar el producto
        boton_guardar = tk.Button(
                                self.ventana_editar,
                                text="Guardar",
                                command=lambda: self.actualizar_producto(
                                    # self.ventana_editar,
                                    self.item_seleccionado,
                                    self.entrada_codigo.get(),
                                    self.entrada_nombre.get(),
                                    self.entrada_precio.get(),
                                    self.entrada_cantidad.get()
                                )
                            )
        boton_guardar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_guardar.place(x=90, y=210 )  

        # -> Botón para cancelar la operación
        boton_cancelar = tk.Button(self.ventana_editar, text="Cancelar", command= self.ventana_editar.destroy)
        boton_cancelar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_cancelar.place(x=260, y=210 )  
#-----------------------------------------------
    def actualizar_producto(self,  item_seleccionado, codigo, nombre, precio, cantidad):
      
        producto_actualizado = Producto(codigo, nombre, precio, cantidad)
        producto_actualizado.id_producto = self.tabla.item(item_seleccionado, "text")  
             
        editar_producto_en_bd(producto_actualizado, producto_actualizado.id_producto)

        # -> Actualiza el Treeview
        self.tabla.item(item_seleccionado, values=(codigo, nombre, precio, cantidad))

        # -> Cierra  la ventana
        self.ventana_editar.destroy()
#-----------------------------------------------
    def eliminar(self):
        self.id_producto = self.tabla.item(self.tabla.selection())['text']

        borrar_producto(self.id_producto)

        self.mostrar_tabla()
#-----------------------------------------------
 
       

       

