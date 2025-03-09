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
        self.busqueda_producto()
#-----------------------------------------------
    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Productos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=380, y=30 )    
#-----------------------------------------------
    def mostrar_tabla(self):
        self.lista_prod = listar_productos()  # --> me trae el listado que capturo con el fetchall
        self.lista_prod.reverse()             # --> invierte el orden sino aparecen en orden de agregado

         # Creo Frame para contener el Treeview y la barra scroll
        frame_tabla = tk.Frame(self)
        frame_tabla.place(x=90, y=100, width=800, height=300)

        self.tabla = ttk.Treeview(frame_tabla, column = ('Codigo','Nombre', 'Precio','Cantidad'))
        self.tabla.place(x =90, y = 100, width=800, height=300) 

        # Creo  barra sroll vertical y la asocio a la tabla
        scrollbar = tk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Posiciono los widgets dentro del frame
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Encabezados de las columnas     
        # self.tabla.heading('#0', text = 'ID') -> columna oculta > pero sigo accediendo al ID
        self.tabla.heading('#0', text='', anchor='center')  # Sin título
        self.tabla.heading('#1', text = 'Codigo', anchor = 'center')
        self.tabla.heading('#2', text = 'Nombre', anchor = 'center')
        self.tabla.heading('#3', text = 'Precio', anchor = 'center')
        self.tabla.heading('#4', text = 'Cantidad', anchor = 'center')

        # Configuración de ancho de columnas
        self.tabla.column('#0', width=0, stretch=tk.NO)  # Oculta la columna ID
        # self.tabla.column ('#0', anchor = 'center', width = 20)
        self.tabla.column ('#1', anchor = 'center', width = 50) #30
        self.tabla.column ('#2', anchor = 'center', width = 150)
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

        self.boton_vender = tk.Button (self, text = 'Vender', command= self.ventas)
        self.boton_vender.config(width = 16, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        self.boton_vender.place(x = 615, y = 510)
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
        
        # -> Obtengo el ID oculto del item seleccionado
        id_producto = self.tabla.item(self.item_seleccionado, "text")  # ID oculto

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
    def ventas(self):
        # -> Obtiene producto seleccionado
        item_seleccionado = self.tabla.selection()
        if not item_seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para vender")
            return

        valores = self.tabla.item(item_seleccionado, "values")
        if not valores:
            messagebox.showerror("Error", "No se pudieron obtener los datos del producto")
            return
        
        codigo, nombre, precio, stock_actual = valores
        stock_actual = int(stock_actual)  # Convertir a entero para cálculos
        
        # -> Creo ventana nueva para agregar un producto
        self.ventana_ventas = tk.Toplevel(self)
        self.ventana_ventas.title("Ventas")
        self.ventana_ventas.config(bg=TITULOS)
        self.ventana_ventas.geometry("500x300+420+180")
        self.ventana_ventas.resizable(0,0)

        # -> Muestra datos en etiquetas
        tk.Label(self.ventana_ventas, text="Código:", bg=TITULOS, fg='white', font=("Nunito", 15, "bold")).place(x=120, y=40)
        label_codigo = tk.Label(self.ventana_ventas, text=codigo, font=('Arial', '14', 'bold'), bg=TITULOS, fg='white')
        label_codigo.place(x=220, y=40)

        tk.Label(self.ventana_ventas, text="Nombre:", bg=TITULOS, fg='white', font=("Nunito", 15, "bold")).place(x=120, y=75)
        label_nombre = tk.Label(self.ventana_ventas, text=nombre, font=('Arial', '14', 'bold'), bg=TITULOS, fg='white')
        label_nombre.place(x=220, y=75)

        tk.Label(self.ventana_ventas, text="Precio:", bg=TITULOS, fg='white', font=("Nunito", 15, "bold")).place(x=120, y=110)
        label_precio = tk.Label(self.ventana_ventas, text=precio, font=('Arial', '14', 'bold'), bg=TITULOS, fg='white')
        label_precio.place(x=220, y=110)

        tk.Label(self.ventana_ventas, text="Stock:", bg=TITULOS, fg='white', font=("Nunito", 15, "bold")).place(x=120, y=145)
        label_stock = tk.Label(self.ventana_ventas, text=stock_actual, font=('Arial', '14', 'bold'), bg=TITULOS, fg='white')
        label_stock.place(x=220, y=145)

        tk.Label(self.ventana_ventas, text="Cantidad a vender:", bg=TITULOS, fg='white', font=("Nunito", 15, "bold")).place(x=120, y=180)
        entrada_cantidad = tk.Entry(self.ventana_ventas, width=6, font=('Arial', '14', 'bold'), fg=BOTONES)
        entrada_cantidad.place(x=310, y=180)


        def confirmar_venta():
            cantidad_vender = entrada_cantidad.get()

            if not cantidad_vender.isdigit():
                messagebox.showerror("Error", "Ingrese una cantidad válida")
                return
            
            cantidad_vender = int(cantidad_vender)

            if cantidad_vender > stock_actual:
                messagebox.showerror("Error", "Stock insuficiente")
                return

            nuevo_stock = stock_actual - cantidad_vender
            producto_actualizado = Producto(codigo, nombre, precio, nuevo_stock)
            producto_actualizado.id_producto = self.tabla.item(item_seleccionado, "text")

            # -> Actualiza BD
            editar_producto_en_bd(producto_actualizado, producto_actualizado.id_producto)

            # -> Actualiza Treeview
            self.tabla.item(item_seleccionado, values=(codigo, nombre, precio, nuevo_stock))

            # -> Cierra ventana
            self.ventana_ventas.destroy()
        
        # -> Botón para vender el producto
        boton_vender = tk.Button(self.ventana_ventas, text="Confirmar Venta", command= confirmar_venta)
        boton_vender.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_vender.place(x= 260, y=235 )  

        # -> Botón para cancelar la operación
        boton_cancelar = tk.Button(self.ventana_ventas, text="Cancelar", command= self.ventana_ventas.destroy)
        boton_cancelar.config(width = 14, font = ('Arial', '12', 'bold'), fg = 'white', bg = SECONDARY,activebackground= BOTONES,cursor='hand2')
        boton_cancelar.place(x= 90, y=235 )  
#-----------------------------------------------
    def busqueda_producto(self):
        # tk.Label(self, text="Producto:", font=("Nunito", 12, "bold"), bg=PRIMARY, fg=TITULOS).place(x= 100, y=510)
      
        self.entry_busqueda = tk.Entry(self, width = 18, font = ('Arial', '13', 'bold'), fg=  BOTONES)
         # -> Agrega el placeholder
        self.entry_busqueda.insert(0, "Buscar producto...") 
        # self.entry_busqueda.config(width = 18, font = ('Arial', '13', 'bold'), fg=BOTONES)
        self.entry_busqueda.place(x=195, y= 510)

        #-> Asocia eventos para manejar el placeholder
        self.entry_busqueda.bind("<FocusIn>", self.on_entry_click)
        self.entry_busqueda.bind("<FocusOut>", self.on_focus_out)

        self.boton_buscar = tk.Button(self, text="Buscar", command=self.buscar_producto)
        self.boton_buscar.config(width = 16, font = ('Arial', '12', 'bold'), fg='white', bg=SECONDARY, activebackground=BOTONES, cursor='hand2')
        self.boton_buscar.place(x = 400, y = 510)
#-----------------------------------------------
    def on_entry_click(self, event):
        """ Borra el placeholder cuando el usuario hace clic en el Entry """
        if self.entry_busqueda.get() == "Buscar producto...":
            self.entry_busqueda.delete(0, tk.END)
            self.entry_busqueda.config(fg= BOTONES)
#-----------------------------------------------
    def on_focus_out(self, event):
        """ Vuelve a colocar el placeholder si el Entry está vacío """
        if self.entry_busqueda.get() == "":
            self.entry_busqueda.insert(0, "Buscar producto...")
            self.entry_busqueda.config(fg= BOTONES)
#-----------------------------------------------
    def buscar_producto(self):
        nombre_buscado = self.entry_busqueda.get().strip().lower()
        
        if not nombre_buscado:
            messagebox.showwarning("Advertencia", "Ingrese un nombre de producto para buscar")
            return
   
        encontrado = False
        
        # -> Itera sobre los elementos del Treeview
        for item in self.tabla.get_children():
            valores = self.tabla.item(item, "values")  # -> Obtiene los valores de la fila
            nombre_producto = valores[1].strip().lower()  # -> Obtiene el nombre del producto
            
            if nombre_buscado in nombre_producto:
                # -> Selecciona el producto encontrado
                self.tabla.selection_set(item)
                self.tabla.focus(item)
                self.tabla.see(item)  # -> Hace scroll hasta el producto encontrado
                encontrado = True
                break
        
        if not encontrado:
            messagebox.showinfo("Información", "Producto no encontrado")

         # Limpia el Entry después de la búsqueda
        self.entry_busqueda.delete(0, tk.END)



     
        

