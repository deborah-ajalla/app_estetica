import tkinter as tk
import datetime
from tkinter import ttk, messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from PIL import Image, ImageTk  


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
        self.boton_buscar_fecha()
        self.boton_reservar()        
      
        self.campos_cargados = False    # Inicialmente los campos de datos están ocultos

    def titulo(self):
        self.titulo = tk.Label(self, text= "✦ Gestión de Turnos ✦ ", font=("Nunito", 22, "bold"), bg=PRIMARY, fg=TITULOS)
        self.titulo.place(x=320, y=30 ) 

    def label(self):
        self.label_fecha = tk.Label(self, text = 'Primera Fecha Disponible: ')
        self.label_fecha.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14, "bold"))
        self.label_fecha.place(x = 285, y = 112)
    
    def entry(self):
        self.fecha_var = tk.StringVar()
        self.fecha_disponible = tk.Entry(self, textvariable = self.fecha_var)
        self.fecha_disponible.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        self.fecha_disponible.place(x = 550, y = 112)

    def boton_buscar_fecha(self):
        self.boton_buscar_fecha = tk.Button (self, text = 'Buscar', command= self.buscar_fecha_turno)
        self.boton_buscar_fecha.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_buscar_fecha.place(x = 345, y = 170)

    def boton_reservar(self):
        self.boton_reservar = tk.Button (self, text = 'Reservar', command= self.reservar_turno)
        self.boton_reservar.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
        self.boton_reservar.place(x = 495, y = 170)

    def carga_datos(self):
        self.label_nombre_turno = tk.Label(self, text = 'Nombre: ')
        self.label_nombre_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
        self.label_nombre_turno.place(x = 215, y = 260)

        self.nombre_turno_var = tk.StringVar()
        self.nombre_turno = tk.Entry(self, textvariable = self.nombre_turno_var)
        self.nombre_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
        
        self.label_apellido_turno = tk.Label(self, text = 'Apellido: ')
        self.label_apellido_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))

        self.apellido_turno_var = tk.StringVar()
        self.apellido_turno = tk.Entry(self, textvariable = self.apellido_turno_var)
        self.apellido_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
    
        self.label_dni_turno = tk.Label(self, text = 'Dni: ')
        self.label_dni_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
    
        self.dni_turno_var = tk.StringVar()
        self.dni_turno = tk.Entry(self, textvariable = self.dni_turno_var)
        self.dni_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
       
        self.label_cel_turno = tk.Label(self, text = 'Celular: ')
        self.label_cel_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
      
        self.cel_turno_var = tk.StringVar()
        self.cel_turno = tk.Entry(self, textvariable = self.cel_turno_var)
        self.cel_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
    
        self.label_mail_turno = tk.Label(self, text = 'Mail: ')
        self.label_mail_turno.config(bg=PRIMARY, fg=BOTONES, font= ("Nunito", 14))
     
        self.mail_turno_var = tk.StringVar()
        self.mail_turno = tk.Entry(self, textvariable = self.mail_turno_var)
        self.mail_turno.config(width = 15, font = ('Arial', '12', 'bold'), fg=BOTONES)
       
        self.cuadro_turno= tk.Text(self, height=9, width=30, padx= 15, pady= 23, font = ('Arial', '11'), fg=BOTONES)
    
        self.boton_guardar_turno = tk.Button (self, text = 'Guardar', command=self.guardar_turno)
        self.boton_guardar_turno.config(width = 12, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_imprimir = tk.Button (self, text = 'Imprimir', command=self.imprimir)
        self.boton_imprimir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_qr = tk.Button (self, text = 'QR', command= self.qr)
        self.boton_qr.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')

        self.boton_limpiar = tk.Button (self, text = 'Limpiar', command= self.limpiar)
        self.boton_limpiar.config(width = 12, font = ('Arial', '12', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
    
    def mostrar_campos_datos(self):  # -> muestro los campos despues de click en reservar
        self.label_nombre_turno.place(x=215, y=260)
        self.nombre_turno.place(x=302, y=260)  # entry

        self.label_apellido_turno.place(x=215, y=300)
        self.apellido_turno.place(x=302, y=300) # entry

        self.label_dni_turno.place(x=215, y=340)
        self.dni_turno.place(x=302, y=340) # entry

        self.label_cel_turno.place(x=215, y=380)
        self.cel_turno.place(x=302, y=380) # entry

        self.label_mail_turno.place(x=215, y=420)
        self.mail_turno.place(x=302, y=420) # entry

        self.cuadro_turno.place(x=490, y=260)  # cuadro de texto

        self.boton_guardar_turno.place(x = 270, y = 480) # botón

        self.boton_imprimir.place(x = 505, y = 480)  # botón

        self.boton_qr.place(x = 630, y = 480)   # botón

        self.boton_limpiar.place(x = 415, y = 540)   # botón

    def buscar_fecha_turno(self):       # -> Habilitar el label de fecha y mostrar una fecha ficticia
        fecha_actual = datetime.date.today()     # -> obtiene la fecha actual
        fecha_disponible = fecha_actual + datetime.timedelta(days=3)  # -> Ej: Primera fecha disponible en 3 días
        self.fecha_var.set(fecha_disponible.strftime("%d/%m/%Y"))     # -> inserta en el 

    def reservar_turno(self):   # -> Capturar los datos ingresados     
        if not self.campos_cargados:
            self.carga_datos()  # Crea los campos solo una vez
            self.mostrar_campos_datos()
            self.campos_cargados = True

    def guardar_turno(self):
        nombre = self.nombre_turno_var.get()
        apellido = self.apellido_turno_var.get()
        dni = self.dni_turno_var.get()
        celular = self.cel_turno_var.get()
        mail = self.mail_turno_var.get()
        fecha = self.fecha_var.get()
       
        if not (nombre and apellido and dni and celular and mail and fecha): # -> Valida que todos los datos estén completos
            messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos antes de reservar.")
            return

        # Muestro los datos en el cuadro de texto
        self.cuadro_turno.delete(1.0, tk.END)  # Limpiar el cuadro
        reserva_texto = f"~~~ Reserva Confirmada ~~~\n\n -   Fecha: {fecha}\n -   Nombre: {(nombre).title()} {(apellido).title()}\n -   DNI: {dni}\n -   Celular: {celular}\n -   Email: {mail} \n~~~~~~~~~~~~~~~~~~~~~~"
        self.cuadro_turno.insert(tk.END, reserva_texto)

        messagebox.showinfo("Reserva Confirmada", "Su turno ha sido reservado correctamente.")
    
    # def imprimir (self):   # -> PARA GUARDAR EL RECIBO COMO ARCHIVO DE TEXTO--- 
    #     info_turno = self.cuadro_turno.get(1.0, )     #guardo el contenido del recibo en una variable
    #     archivo = filedialog.asksaveasfile(mode='w', defaultextension= '.txt')  #guardo en un archivo txt
    #     archivo.write(info_turno)   #escribo el recibo
    #     archivo.close()              #cierro el archivo
    #     messagebox.showinfo('Informacion', 'Su Recibo Ha Sido Guardado!') #abre una ventana cuando ya guardé el archivo de texto

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
        self.dni_turno_var.set("")
        self.cel_turno_var.set("")
        self.mail_turno_var.set("")
        self.cuadro_turno.delete(1.0, tk.END)  # -> Limpia el cuadro de texto

        # -> Si existe un Label para el QR, lo elimina
        if hasattr(self, "qr_label"):
            self.qr_label.destroy()
            del self.qr_label  # -> Elimina la referencia para evitar errores