import sqlite3
#------------------------------------------------------------
class Conexion():
    def __init__(self): 
        self.conexion = sqlite3.connect("estetica.db")
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()

