import tkinter as tk
from vista.ventana import Aplicacion, barra_menu



def main():
    # se crea ventana gráfica
    ventana = tk.Tk()
    ventana.title("Centro de Estética")
    ventana.geometry("1000x600+160+50")
    ventana.resizable(0,0)
   
    barra_menu(ventana)
    app = Aplicacion(root=ventana)

    # -> para que la ventana se mantenga abierta
    ventana.mainloop()

if __name__ == '__main__':
    main()