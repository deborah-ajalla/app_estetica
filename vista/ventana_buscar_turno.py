import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ddbb.consultas import listar_pacientes_por_dni, obtener_turnos_por_dni
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

        if not dni:  # Si el campo está vacío, no mostrar advertencia de inmediato
            messagebox.showwarning("Advertencia", "Por favor, ingrese un DNI...")
            return  

        paciente = listar_pacientes_por_dni(dni)

        if not hasattr(self, 'cuadro_turno'): # si no hay cuadro de texto -> lo crea
            self.cuadro_turno = tk.Text(self, height=11, width=40, padx= 30, pady= 30, font = ('Arial', '12', 'bold'), fg=BOTONES)
            self.cuadro_turno.place(x = 267, y = 240)

        self.cuadro_turno.delete("1.0", tk.END)

        if paciente:
            
            nombre = paciente[0].title()
            apellido = paciente[1].title()
            celular = paciente[3]
            email = paciente[4]

            # Obtener turnos del paciente
            turnos = obtener_turnos_por_dni(dni)

            # Construir el mensaje
            info_paciente = f"         ~~~ DATOS DEL PACIENTE ~~~\n\n -  Nombre: {nombre}\n -  Apellido: {apellido}\n -  DNI: {dni}\n -  Celular: {celular}\n -  Email: {email}\n\n"

            if turnos:
                info_turnos = "         ~~~ TURNOS REGISTRADOS ~~~\n"
                for fecha, horario in turnos:
                    info_turnos += f"\n - {fecha} a las {horario} hs"
                info_turnos += "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
            else:
                info_turnos = "\nNo tiene turnos registrados."

            # Insertar datos en el cuadro de texto
            self.cuadro_turno.insert(tk.END, info_paciente + info_turnos)
    
    # else:
    #     messagebox.showerror("Error", "No se encontró un paciente con ese DNI")



            # self.cuadro_turno.insert(tk.END, f"         ~~~ SU PRÓXIMO TURNO ~~~\n\n -  Fecha: \n\n -  Nombre: {paciente[0].title()}\n -  Apellido: {paciente[1].title()}\n -  DNI: {paciente[2]}\n -  Celular: {paciente[3]}\n -  Email: {paciente[4]}")

            if not hasattr(self, 'boton_imprimir'):
                self.boton_imprimir = tk.Button (self, text = 'Imprimir', command=self.imprimir)
                self.boton_imprimir.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
                self.boton_imprimir.place(x = 355, y = 530)

            if not hasattr(self, 'boton_qr'):
                self.boton_qr = tk.Button (self, text = 'QR', command= self.qr)
                self.boton_qr.config(width = 11, font = ('Arial', '11', 'bold'), fg = '#FFFFFF', bg = SECONDARY, activebackground= BOTONES,cursor='hand2')
                self.boton_qr.place(x = 494, y = 530)

        else:
            messagebox.showwarning("ADVERTENCIA!", "EL DNI INGRESADO NO ESTÁ REGISTRADO...")
            # self.cuadro_turno.insert(tk.END, "Debe ingresar un DNI para comenzar la búsqueda...")

    def limpiar(self):
        self.dni_var.set("")   # -> Borra el contenido del Entry
        self.cuadro_turno.delete(1.0, tk.END)  # -> Limpia el cuadro de texto

          
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