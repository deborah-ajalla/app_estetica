import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ddbb.consultas import listar_pacientes_por_dni, obtener_turnos_por_dni, actualizar_turno_en_bd, obtener_id_profesional
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from PIL import Image, ImageTk  

#----------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"
BOTONES = "#805AD5"

class Buscar_Turnos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=TITULOS)
        self.place(x=0, y=0, width=1000, height=600) 
        
        self.titulo()
        self.label()
        self.entry()
        self.boton_buscar()
        self.boton_limpiar()
        self.frame_turno = None  # Inicialmente no existe el frame

    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Búsqueda de Turnos ✦ ", font=("Nunito", 22, "bold"), fg='white', bg=TITULOS)
        self.titulo.place(x=290, y=35)
    
    def label(self):
        self.label_dni_buscado = tk.Label(self, text = 'Ingrese el Dni: ')
        self.label_dni_buscado.config( fg='white', bg=TITULOS, font= ("Nunito", 14, "bold"))
        self.label_dni_buscado.place(x = 335, y = 100)
    
    def entry(self):
        self.dni_var = tk.StringVar()
        self.dni_buscado = tk.Entry(self, textvariable = self.dni_var)
        self.dni_buscado.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.dni_buscado.place(x = 485, y = 100)

    def boton_buscar(self):
        self.boton_buscar = tk.Button (self, text = 'Buscar', command= self.buscar_turno_por_dni)
        self.boton_buscar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar.place(x = 355, y = 160)
    
    def boton_limpiar(self):
        self.boton_limpiar = tk.Button (self, text = 'Limpiar', command= self.limpiar)
        self.boton_limpiar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_limpiar.place(x = 494, y = 160)

    def buscar_turno_por_dni(self):
        dni = self.dni_buscado.get().strip()

        if not dni:  
            messagebox.showwarning("Advertencia", "Por favor, ingrese un DNI...")
            return  

        paciente = listar_pacientes_por_dni(dni)

        # -> Si ya existe un frame, eliminarlo antes de crear uno nuevo
        if self.frame_turno:
            self.frame_turno.destroy()

        # -> Crea un nuevo frame para contener el cuadro de texto y la barra scroll
        self.frame_turno = tk.Frame(self)
        self.frame_turno.place(x=267, y=240)
 
        if paciente:       
            nombre = paciente[0].title()
            apellido = paciente[1].title()
            celular = paciente[3]
            email = paciente[4]
    
            turnos = obtener_turnos_por_dni(dni)    # -> Obtiene turnos del paciente

            #  -> Mensaje
            info_paciente = f"          ~~~ DATOS DEL PACIENTE ~~~\n\n    -  Nombre: {nombre} {apellido}\n    -  DNI: {dni}\n    -  Celular: {celular}\n    -  Email: {email}\n\n\n"


            #-> Treeview para listar los turnos
            columnas = ("Fecha", "Horario", "Profesional")
            self.tabla_turnos = ttk.Treeview(self.frame_turno, columns=columnas, show="headings", height=6)

            # -> Definio estilo para filas personalizadas
            self.tabla_turnos.tag_configure("deborah", background="#FFB6C1")  # Rosa claro

            for col in columnas:
                 self.tabla_turnos.heading(col, text=col)
                 self.tabla_turnos.column(col, width=150)

            # -> Agregar Scrollbar vertical
            scroll_y = ttk.Scrollbar(self.frame_turno, orient="vertical", command=self.tabla_turnos.yview)
            self.tabla_turnos.configure(yscrollcommand=scroll_y.set)

            self.tabla_turnos.place(x=0, y=500, width=510, height=160)  
            scroll_y.place(x=500, y=0, height=160)  
       
            # Insertar turnos en el Treeview
            for idx, (fecha, horario, nombre_prof, apellido_prof) in enumerate(turnos):
                profesional = f"{nombre_prof} {apellido_prof}"
                # Si el profesional es "Deborah Ajalla", usar el tag "deborah"
                tag = "deborah" if profesional.lower() == "deborah ajalla" else ""
                self.tabla_turnos.insert("", "end", iid=idx, values=(fecha, horario, profesional), tags=(tag,))

                self.tabla_turnos.pack()

            if not hasattr(self, 'boton_modificar'):
                self.boton_modificar = tk.Button (self, text = 'Modificar', command= self.modificar_turno)
                self.boton_modificar.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
                self.boton_modificar.place(x = 278, y = 460)
        
            if not hasattr(self, 'boton_imprimir'):
                self.boton_imprimir = tk.Button (self, text = 'Imprimir', command=self.imprimir)
                self.boton_imprimir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
                self.boton_imprimir.place(x = 435, y = 460)

            if not hasattr(self, 'boton_qr'):
                self.boton_qr = tk.Button (self, text = 'QR', command= self.qr)
                self.boton_qr.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
                self.boton_qr.place(x = 585, y = 460)
        else:
            messagebox.showwarning("ADVERTENCIA!", "EL DNI INGRESADO NO ESTÁ REGISTRADO...")
            # self.cuadro_turno.insert(tk.END, "Debe ingresar un DNI para la búsqueda...")

    def limpiar(self):
        self.dni_var.set("")   # -> Borra el contenido del Entry
        self.tabla_turnos.delete(1.0, tk.END)  # -> Limpia el cuadro de texto

        self.dni_buscado.focus_set()    # -> Coloca el cursor en el Entry de Fecha Disponible
         
        if hasattr(self, "qr_label"): # -> Si existe un Label para el QR, lo elimina
            self.qr_label.destroy()
            del self.qr_label  # -> Elimina la referencia para evitar errores

    def imprimir(self):
        contenido = self.cuadro_turno.get(1.0, tk.END).strip()
        if not contenido:
            messagebox.showwarning("Imprimir", "No hay contenido para guardar.")
            return

        archivo_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        if archivo_pdf:
            c = canvas.Canvas(archivo_pdf, pagesize=letter)       # -> Crea el PDF
            c.setFont("Helvetica", 12)                            # -> establece fuente y tamaño del texto.
            c.drawString(100, 750, "    ✦ Reserva de Turno ✦")   # -> título
            
            y = 730  # -> Posición inicial del texto
            for linea in contenido.split("\n"):
                c.drawString(100, y, linea)
                y -= 20  # ->  Espaciado entre líneas

            c.save()     # -> finaliza y guarda el PDF.
            messagebox.showinfo("Éxito", f"El archivo PDF se ha guardado correctamente en:\n{archivo_pdf}")  

    def qr (self):
        contenido = self.cuadro_turno.get(1.0, tk.END).strip()
        if not contenido:
            messagebox.showwarning("Código QR", "No hay contenido para generar el código QR.")
            return
    
        qr_img = qrcode.make(contenido)    #  -> Crea el código QR
        
        qr_img_path = "turno_qr.png"       #  -> Guarda el código QR en un archivo temporal
        qr_img.save(qr_img_path)
   
        img = Image.open(qr_img_path)      # -> Muestra el código QR en la interfaz
        img = img.resize((200, 200))       # -> Redimensiona la imagen para que encaje en la ventana
        self.qr_photo = ImageTk.PhotoImage(img)  # -> Convierte la imagen para Tkinter
      
        if hasattr(self, "qr_label"):          # -> Crea o actualiza el Label con la imagen QR
            self.qr_label.config(image=self.qr_photo)
        else:
            self.qr_label = tk.Label(self, image=self.qr_photo, bg=PRIMARY)
            self.qr_label.place(x=765, y=40)  # -> Ubicación en la interfaz

        messagebox.showinfo("Código QR", "El código QR se ha generado correctamente.")

    def modificar_turno(self):
        seleccionado = self.tabla_turnos.selection()

        if not seleccionado:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un turno para modificar.")
            return

        # -> Obtiene el índice (ID) del turno seleccionado
        self.idx_seleccionado = seleccionado[0]     

        # -> Obtiene los valores de la fila seleccionada
        valores = self.tabla_turnos.item(self.idx_seleccionado, "values")
        # fecha_anterior, horario_anterior, profesional = valores
        if not valores:
            messagebox.showerror("Error", "No se pudo obtener la información del turno.")
            return
      
        fecha, horario,profesional = valores
         
        # Crear la ventana de modificación
        self.ventana_modificar = tk.Toplevel(self)
        self.ventana_modificar.title("Modificar Turno")
        self.ventana_modificar.config(bg=PRIMARY)
        self.ventana_modificar.geometry("450x280+0+280")
        self.ventana_modificar.resizable(0, 0)

        # -> Creo variables para los Entry
        self.fecha_mod_var = tk.StringVar(value=fecha)
        self.hora_mod_var = tk.StringVar(value=horario)
        self.profesional_mod_var = tk.StringVar(value=profesional)

        # -> Etiquetas label
        tk.Label(self.ventana_modificar, text="Fecha:", bg=PRIMARY, fg=BOTONES, font=("Nunito", 15, "bold")).place(x=80, y=40)
        entrada_fecha = tk.Entry(self.ventana_modificar, textvariable=self.fecha_mod_var, width=17, font=('Arial', '12', 'bold'), fg=BOTONES)
        entrada_fecha.place(x=210, y=40)

        tk.Label(self.ventana_modificar, text="Horario:", bg=PRIMARY, fg=BOTONES, font=("Nunito", 15, "bold")).place(x=80, y=80)
        entrada_horario = tk.Entry(self.ventana_modificar, textvariable=self.hora_mod_var, width=17, font=('Arial', '12', 'bold'), fg=BOTONES)
        entrada_horario.place(x=210, y=80)

        tk.Label(self.ventana_modificar, text="Profesional:", bg=PRIMARY, fg=BOTONES, font=("Nunito", 15, "bold")).place(x=80, y=120)
        entrada_profesional = tk.Entry(self.ventana_modificar, textvariable=self.profesional_mod_var, width=17, font=('Arial', '12', 'bold'), fg=BOTONES)
        entrada_profesional.place(x=210, y=120)

        # -> Botones
        tk.Button(self.ventana_modificar, text="Editar", command=self.guardar_cambios, width=14, font=('Arial', '12', 'bold'), fg='white', bg=SECONDARY, activebackground=BOTONES, cursor='hand2').place(x=60, y=190)

        tk.Button(self.ventana_modificar, text="Cancelar", command=self.ventana_modificar.destroy, width=14, font=('Arial', '12', 'bold'), fg='white', bg=SECONDARY, activebackground=BOTONES, cursor='hand2').place(x=230, y=190)


    # Función para actualizar datos
    def guardar_cambios(self):
        nueva_fecha = self.fecha_mod_var.get()
        nuevo_horario = self.hora_mod_var.get()
        nuevo_profesional = self.profesional_mod_var.get().strip()  # Quita espacios extra

         # -> Verifica que el nombre del profesional tiene al menos dos partes (nombre y apellido)
        partes = nuevo_profesional.split()
        if len(partes) < 2:
            messagebox.showerror("Error", "El nombre del profesional debe incluir nombre y apellido.")
            return
        
        nombre_profesional = partes[0]  # Primera palabra como nombre
        apellido_profesional = " ".join(partes[1:])  # Resto como apellido

         # -> Obtener el ID del profesional (usando el nombre y apellido)
        nuevo_id_profesional = obtener_id_profesional(nombre_profesional, apellido_profesional)

        # -> Obtiene el índice del turno seleccionado
        idx = self.idx_seleccionado  
    
        # -> Obtiene los valores originales del turno seleccionado
        valores_originales = self.tabla_turnos.item(idx, "values")
        fecha_original, horario_original, profesional_original = valores_originales

        # -> Llamo a la función para actualizar el turno en la BD-
        exito = actualizar_turno_en_bd( nueva_fecha, nuevo_horario, nuevo_id_profesional,fecha_original, horario_original, profesional_original)

        if exito:       
            # -> Actualizo Treeview
            self.tabla_turnos.item(idx, values=(nueva_fecha, nuevo_horario, nuevo_profesional))

            # -> Deselecciona la fila después de la actualización
            self.tabla_turnos.selection_remove(self.idx_seleccionado)
       
            messagebox.showinfo("Éxito", "Turno actualizado correctamente.")
            self.ventana_modificar.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el turno.")

       
                