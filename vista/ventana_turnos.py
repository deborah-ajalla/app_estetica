import tkinter as tk
import datetime
from tkinter import ttk, messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from PIL import Image, ImageTk  
from ddbb.consultas import buscar_por_dni_en_tto, verificar_horario_ocupado, listar_profesionales_combobox,obtener_id_profesional, obtener_nombre_apellido_profesional, turno_ocupado_para_profesional, guardar_turno_en_bd
#--------------------------------
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
        self.cargar_profesionales()
        self.boton_buscar_fecha()
        self.boton_reservar()        
      
        self.campos_cargados = False    # Inicialmente los campos de datos están ocultos

    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Gestión de Turnos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=320, y= 25 ) 

    def label(self):
        self.label_profesional = tk.Label(self, text = ' Profesional: ')
        self.label_profesional.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14, "bold"))
        self.label_profesional.place(x = 315, y = 80)

        self.label_fecha = tk.Label(self, text = 'Fecha Disponible: ')
        self.label_fecha.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14, "bold"))
        self.label_fecha.place(x = 315, y = 115)

        self.label_hora = tk.Label(self, text = 'Elegir Horario : ')
        self.label_hora.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14, "bold"))
        self.label_hora.place(x = 315, y = 150)
           
    def entry(self):
        self.profesional_var = tk.StringVar()  # -> Variable para el horario seleccionado 
        self.combo_profesinales = ttk.Combobox(self, textvariable=self.profesional_var, state="readonly")
        self.combo_profesinales.place(x=535, y=80)

        # -> Carga profesionales en el Combobox
        self.cargar_profesionales()

        self.fecha_var = tk.StringVar()
        self.fecha_disponible = tk.Entry(self, textvariable = self.fecha_var)
        self.fecha_disponible.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.fecha_disponible.place(x = 535, y = 115)
  
        self.horarios = ["08:00", "09:30", "11:00", "12:30", "15:00", "16:30", "18:00"]   # -> Lista de horarios disponibles 
        self.hora_var = tk.StringVar()     # -> Variable para el horario seleccionado  
        self.combo_horarios = ttk.Combobox(self, textvariable=self.hora_var, values=self.horarios, state="readonly")   # -> Desplegable de horarios
        self.combo_horarios.place(x = 535, y = 150)

    def boton_buscar_fecha(self):
        self.boton_buscar_fecha = tk.Button (self, text = 'Buscar', command= self.buscar_fecha_turno)
        self.boton_buscar_fecha.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar_fecha.place(x = 355, y = 190)

    def boton_reservar(self):
        self.boton_reservar = tk.Button (self, text = 'Reservar', command= self.reservar_turno)
        self.boton_reservar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_reservar.place(x = 505, y = 190)

    def cargar_profesionales(self):
        lista = listar_profesionales_combobox()  # -> Obtiene los nombres desde la BD
        self.combo_profesinales["values"] = lista  # -> Asigna la lista al Combobox

    def carga_datos(self):

        self.label_dni_buscado = tk.Label(self, text = 'Dni: ')
        self.label_dni_buscado.config(bg= PRIMARY, fg= BOTONES, font= ("Nunito", 14, "bold"))
       
        self.dni_var = tk.StringVar()
        self.dni_buscado = tk.Entry(self, textvariable = self.dni_var)
        self.dni_buscado.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
  
        self.boton_buscar = tk.Button (self, text = ' 🔍', command= self.buscar_por_dni)
        self.boton_buscar.config(width = 10, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
       
        self.label_nombre_turno = tk.Label(self, text = 'Nombre: ')
        self.label_nombre_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
      
        self.nombre_turno_var = tk.StringVar()
        self.nombre_turno = tk.Entry(self, textvariable = self.nombre_turno_var)
        self.nombre_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        
        self.label_apellido_turno = tk.Label(self, text = 'Apellido: ')
        self.label_apellido_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))

        self.apellido_turno_var = tk.StringVar()
        self.apellido_turno = tk.Entry(self, textvariable = self.apellido_turno_var)
        self.apellido_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
           
        self.cuadro_turno= tk.Text(self, height=9, width=30, padx= 15, pady= 23, font = ('Arial', '11'), fg=BOTONES)
    
        self.boton_guardar_turno = tk.Button (self, text = 'Guardar', command=self.guardar_turno)
        self.boton_guardar_turno.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_imprimir = tk.Button (self, text = 'Imprimir', command=self.imprimir)
        self.boton_imprimir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_qr = tk.Button (self, text = 'QR', command= self.qr)
        self.boton_qr.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_limpiar = tk.Button (self, text = 'Limpiar', command= self.limpiar)
        self.boton_limpiar.config(width = 11, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
    
    def mostrar_campos_datos(self):  # -> muestro los campos despues de click en reservar
        self.label_dni_buscado.place(x = 196, y = 264)
        self.dni_buscado.place(x = 270, y = 264)

        self.boton_buscar.place(x = 250, y = 310)

        self.label_nombre_turno.place(x=180, y=370)
        self.nombre_turno.place(x=270, y=370)  # entry

        self.label_apellido_turno.place(x=180, y=415)
        self.apellido_turno.place(x=270, y=415) # entry

        self.cuadro_turno.place(x=490, y=260)  # cuadro de texto

        self.boton_guardar_turno.place(x = 245, y = 480) # botón

        self.boton_imprimir.place(x = 505, y = 480)  # botón

        self.boton_qr.place(x = 630, y = 480)   # botón

        self.boton_limpiar.place(x = 415, y = 540)   # botón

    def buscar_fecha_turno(self):       # -> Habilitar el label de fecha y mostrar una fecha ficticia
        fecha_actual = datetime.date.today()     # -> obtiene la fecha actual
        fecha_disponible = fecha_actual + datetime.timedelta(days=3)  # -> Ej: Primera fecha disponible en 3 días
        self.fecha_var.set(fecha_disponible.strftime("%d/%m/%Y"))     # -> inserta en el 

    def reservar_turno(self):     
        horario = self.hora_var.get().strip()
        fecha = self.fecha_var.get().strip()

        if not horario:  # -> Si el campo está vacío, no mostrar advertencia de inmediato
            messagebox.showwarning("Advertencia", "Por favor, ingrese un Horario...")
            return  
        
        # -> Valida si la fecha ingresada es pasada
        fecha_actual = datetime.datetime.today().date()  #->  Obtiene la fecha de hoy
        try:
            fecha_seleccionada = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()  # -> Convierte la fecha del Entry a formato date
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use DD/MM/YYYY.")
            return

        if fecha_seleccionada < fecha_actual:
            messagebox.showwarning("Fecha Inválida", "No puede reservar un turno en una fecha pasada...")
            return

        # ->  Obtiene los horarios ocupados en la fecha seleccionada
        horarios_ocupados = self.obtener_horarios_ocupados(fecha)
        
        # -> Actualiza el combobox con los horarios disponibles
        self.actualizar_horarios_combobox(horarios_ocupados)
        
        # -> Verifica si el turno en la fecha y hora seleccionada ya está ocupado
        if horario in horarios_ocupados:
            messagebox.showwarning("Turno Ocupado", "El turno en esa fecha y horario ya está ocupado. Elija otro.")
            return
        
        # -> Verifica si el profesional ya tiene un turno reservado para ese horario
        profesional = self.profesional_var.get().strip()

        #  -> Verifica si se ha seleccionado un profesional
        if not profesional:
            messagebox.showwarning("Advertencia", "Seleccione un profesional antes de continuar.")
            return

        # -> Separa nombre y apellido asegurando que hay dos partes
        partes = profesional.split()

        if len(partes) != 2:  # -> Esto evita errores si hay más o menos de dos palabras
            messagebox.showerror("Error", "Formato del nombre del profesional incorrecto.")
            return
        
        nombre_profesional, apellido_profesional = partes
        
        # Obtiene el ID del profesional
        id_profesional = obtener_id_profesional(nombre_profesional, apellido_profesional)
        
        if id_profesional is None:
            messagebox.showerror("Error", "No se encontró el profesional en la base de datos.")
            return
        
        # Verifica si el profesional ya tiene un turno reservado para ese horario
        if turno_ocupado_para_profesional(id_profesional, fecha, horario):
            messagebox.showwarning("Profesional Ocupado", f"El profesional {profesional} ya tiene un turno a esta hora.")
            return

        if not self.campos_cargados:
            self.carga_datos()  # Crea los campos solo una vez
            self.mostrar_campos_datos()
            self.campos_cargados = True

    def obtener_horarios_ocupados(self, fecha):      
        horarios_ocupados = verificar_horario_ocupado(fecha)  # Esta función debe devolver una lista de horarios ocupados
        
        return horarios_ocupados
    
    def actualizar_horarios_combobox(self, horarios_ocupados): # ->  desactiva los horarios ocupados.
        horarios_disponibles = ["08:00", "09:30", "11:00", "12:30", "15:00", "16:30", "18:00"]
        
        # -> Filtra los horarios disponibles, excluyendo los ocupados
        horarios_actualizados = [hora for hora in horarios_disponibles if hora not in horarios_ocupados]
        
        # -> Se Actualizan los valores del combobox con los horarios disponibles
        self.combo_horarios.config(values=horarios_actualizados)
        
        # -> Si no hay horarios disponibles, muestra mensaje
        if not horarios_actualizados:
            messagebox.showwarning("Sin Horarios Disponibles", "No hay horarios disponibles para esta fecha.")

    def buscar_por_dni(self):
        self.dni_buscado.focus_set() 
        dni = self.dni_buscado.get().strip()

        if not dni:  # -> Si el campo está vacío, no mostrar advertencia de inmediato
            messagebox.showwarning("Advertencia", "Por favor, ingrese un DNI...")
            return  
        
        paciente = buscar_por_dni_en_tto (dni) # -> importo de la bd

        if paciente:  # -> Si el paciente existe, lleno los entrys
            self.nombre_turno_var.set(paciente[0].title())
            self.apellido_turno_var.set(paciente[1].title())
        else:
            messagebox.showerror("Error", "No se encontró un paciente con ese DNI")

    def guardar_turno(self):
        nombre = self.nombre_turno_var.get()
        apellido = self.apellido_turno_var.get()
        dni = self.dni_var.get()
        profesional = self.profesional_var.get()
        fecha = self.fecha_var.get()
        horario = self.hora_var.get() 
       
        if not (nombre and apellido and dni and profesional and fecha and horario): # -> Valida que todos los datos estén completos
            messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos antes de reservar.")
            return
        
        nombre_profesional, apellido_profesional = profesional.split()  # Asumiendo que es 'nombre apellido'
        
        # -> Obtiene el ID del profesional
        id_profesional = obtener_id_profesional(nombre_profesional, apellido_profesional)
        
        if id_profesional is None:
            messagebox.showerror("Error", "No se encontró el profesional en la base de datos.")
            return
           
        if guardar_turno_en_bd(dni, fecha, horario, id_profesional): # -> Guarda en la BD

            # -> Obtiene el nombre y apellido del profesional
            nombre_prof, apellido_prof = obtener_nombre_apellido_profesional(id_profesional)
            self.cuadro_turno.delete(1.0, tk.END)    # ->  Limpia el cuadro de texto
            reserva_texto = f"~~~ Reserva Confirmada ~~~\n\n - Fecha: {fecha}\n - Horario: {horario}\n - Nombre: {nombre.title()} {apellido.title()}\n - DNI: {dni}\n - Profesional: {nombre_prof} {apellido_prof}\n\n~~~~~~~~~~~~~~~~~~~~~~"
            self.cuadro_turno.insert(tk.END, reserva_texto)
        else:
            messagebox.showerror("Error", "No se pudo guardar el turno en la base de datos.") 
            
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
            self.qr_label.place(x=780, y=40)  # -> Ubicación en la interfaz

        messagebox.showinfo("Código QR", "El código QR se ha generado correctamente.")

    def limpiar(self):
        self.fecha_var.set("")
        self.nombre_turno_var.set("")
        self.apellido_turno_var.set("")
        self.dni_var.set("")
        self.hora_var.set("")  # -> Limpia el combobox
        self.cuadro_turno.delete(1.0, tk.END)  # -> Limpia el cuadro de texto
    
        self.fecha_disponible.focus_set()    # -> Coloca el cursor en el Entry de Fecha Disponible

        # -> Si existe un Label para el QR, lo elimina
        if hasattr(self, "qr_label"):
            self.qr_label.destroy()
            del self.qr_label  # -> Elimina la referencia para evitar errores