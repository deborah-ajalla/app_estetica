import sqlite3
from .conexion import Conexion
from tkinter import messagebox
#------------------------------------------
def crear_tabla():
    cone = Conexion()

    sql = """
              CREATE TABLE IF NOT EXISTS pacientes
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NOMBRE TEXT NOT NULL,
              APELLIDO TEXT NOT NULL,
              DNI TEXT NOT NULL UNIQUE,
              CELULAR TEXT NOT NULL UNIQUE,
              MAIL TEXT NOT NULL UNIQUE,
              ID_TRATAMIENTOS INTEGER,
              ID_PRODUCTOS INTEGER,
              FOREIGN KEY(ID_TRATAMIENTOS) REFERENCES tratamientos(id),
              FOREIGN KEY(ID_PRODUCTOS) REFERENCES productos(id)
              );

               CREATE TABLE IF NOT EXISTS tratamientos
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              NOMBRE_t TEXT NOT NULL,
              DNI TEXT NOT NULL,  
              PROCEDIMIENTO TEXT NOT NULL,
              FOREIGN KEY (dni) REFERENCES pacientes(dni)
              );

              CREATE TABLE IF NOT EXISTS productos
             (
              ID_PRODUCTOS INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
              CODIGO INTEGER NOT NULL,
              NOMBRE TEXT NOT NULL,
              PRECIO INTEGER NOT NULL,
              CANTIDAD TEXT NOT NULL        
              );

               CREATE TABLE IF NOT EXISTS turnos
              (
              ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              DNI TEXT NOT NULL,
              FECHA TEXT NOT NULL,
              HORARIO TEXT NOT NULL,
              ID_PROFESIONAL INTEGER NOT NULL,
              FOREIGN KEY (DNI) REFERENCES pacientes(DNI),
              FOREIGN KEY (ID_PROFESIONAL) REFERENCES profesionales(ID_PROFESIONAL)
              );

              CREATE TABLE IF NOT EXISTS profesionales (
              ID_PROFESIONAL INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              NOMBRE TEXT NOT NULL,
              APELLIDO TEXT NOT NULL,
              DNI INTEGER NOT NULL,
              CEL INTEGER NOT NULL,
              MAIL TEXT NOT NULL,
              ESPECIALIDAD TEXT NOT NULL
              );

            """
    try:
        cone.cursor.executescript(sql)
    except Exception as e:
        print("Error al crear tablas:", e)
    finally:
        cone.cerrar_conexion()
#------------------------------------------
class Paciente():
    def __init__(self, nombre, apellido, dni, cel, mail):
        self.id_paciente = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cel = cel
        self.mail = mail

    def __str__(self):
        return f'Paciente[{self.nombre}, {self.apellido}, {self.dni}, {self.cel}, {self.mail}]'
#------------------------------------------
def guardar_paciente(paciente):
    cone = Conexion()

    sql= f'''
             INSERT INTO pacientes(Nombre,Apellido,Dni, Celular, Mail)
             VALUES('{paciente.nombre}','{paciente.apellido}','{paciente.dni}','{paciente.cel}','{paciente.mail}');
        '''
    try:
        cone.cursor.execute(sql)
    except:
        pass
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def listar_pacientes():
    cone = Conexion()
    listar_pacientes = []
   
    sql = f'''
            SELECT * FROM pacientes as p
           
          '''
    try:
        cone.cursor.execute(sql)
        listar_pacientes = cone.cursor.fetchall()

        return listar_pacientes
    except:
        pass
    finally:
       cone.cerrar_conexion()
#------------------------------------------
def listar_tratamientos():
    cone = Conexion()

    listar_tratamiento = []

    sql = f'''
           SELECT * FROM tratamientos;
          '''
    try:
        cone.cursor.execute(sql)
        listar_tratamiento = cone.cursor.fetchall()

        return listar_tratamiento
    except:
        pass
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def editar_paciente(paciente, id):
    cone = Conexion()   
    
    # sql= f'''
    #          UPDATE pacientes
    #          SET NOMBRE = '{paciente.nombre}',
    #            APELLIDO = '{paciente.apellido}',
    #            DNI = '{paciente.dni}', 
    #            CELULAR = '{paciente.cel}', 
    #            MAIL = '{paciente.mail}'
    #           WHERE ID = {id};
    #           ;
    # '''

    sql= f"""
         UPDATE pacientes
         SET NOMBRE = ?,
         APELLIDO = ?,
         DNI = ?,
         CELULAR = ?,
         MAIL = ?
         WHERE ID = ?;
"""
    try:
        cone.cursor.execute(sql, (paciente.nombre, paciente.apellido,paciente.dni, paciente.cel,paciente.mail, id))
        cone.cerrar_conexion()
        # cone.cursor.commit()
    except:
        pass
       
#------------------------------------------
def borrar_paciente(id):
    cone = Conexion()

    sql= f'''
         DELETE FROM pacientes WHERE ID = {id};
         '''
    try:
        cone.cursor.execute(sql)
    except:
        pass
    finally:
        cone.cerrar_conexion()

#------------------------------------------
def listar_pacientes_por_dni(dni):
    cone = Conexion()  # Conectar a la base de datos
    try:
        sql = "SELECT nombre, apellido, dni, celular, mail FROM pacientes WHERE dni = ?"
        cone.cursor.execute(sql, (dni,))
        paciente = cone.cursor.fetchone()  # Obtener el primer resultado encontrado
    except Exception as e:
        print(f"Error en la consulta: {e}")
        paciente = None
    finally:
        cone.cerrar_conexion()  # Cerrar la conexión a la base de datos
    return paciente  # Retorna una tupla con los datos o None si no encuentra el paciente
#------------------------------------------
class Tratamiento():

    def __init__(self, nombre_t, dni, procedimiento):
        self.id_paciente = None
        self.nombre_t = nombre_t
        self.dni = dni
        self.procedimiento = procedimiento   

    def __str__(self):
        return f'Tratamiento [{self.nombre_t}, {self.dni}, {self.procedimiento}]'
#------------------------------------------
def guardar_tratamiento(tratamiento):
    cone = Conexion()

    sql= f'''
              INSERT INTO tratamientos(Nombre_t,Dni,Procedimiento)
              VALUES('{tratamiento.nombre_t}','{tratamiento.dni}','{tratamiento.procedimiento}');
         '''
    try:
        cone.cursor.execute(sql)
    except  Exception as e:
        print(f"Error al guardar el tratamiento: {e}")  # Mostrar error en consola
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def buscar_por_dni_en_tto(dni):
    cone = Conexion()  # Conectar a la base de datos
    try:
        sql = "SELECT nombre, apellido FROM pacientes WHERE dni = ?"
        cone.cursor.execute(sql, (dni,))
        paciente = cone.cursor.fetchone()  # Obtener el primer resultado encontrado
    except Exception as e:
        print(f"Error en la consulta: {e}")
        paciente = None
    finally:
        cone.cerrar_conexion()  # Cerrar la conexión a la base de datos
    return paciente  # Retorna una tupla con los datos o None si no encuentra el paciente
#------------------------------------------
def buscar_tratamientos_por_dni(dni):
    cone = Conexion()  # Conectar a la base de datos
    try:
        sql = "SELECT nombre_t, procedimiento FROM tratamientos WHERE dni = ?"
        cone.cursor.execute(sql, (dni,))
        tratamiento = cone.cursor.fetchall()
    
    except Exception as e:
        print(f"Error en la consulta: {e}")
        tratamiento = None
    finally:
        cone.cerrar_conexion()  # Cerrar la conexión a la base de datos
    return tratamiento  # Retorna una tupla con los datos o None si no encuentra el paciente
#------------------------------------------
def verificar_turno_ocupado(fecha, horario):
    cone = Conexion()
    sql = "SELECT COUNT(*) FROM turnos WHERE FECHA = ? AND HORARIO = ?"

    try:
        cone.cursor.execute(sql, (fecha, horario))
        resultado = cone.cursor.fetchone()
        return resultado[0] > 0  # -> Retorna True si el turno está ocupado
    except Exception as e:
        print("Error al verificar el turno:", e)
        return False
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def verificar_horario_ocupado(fecha):    # ->devuelve una lista de horarios ocupados
    cone = Conexion()
    sql = "SELECT horario FROM turnos WHERE fecha = ?"
    
    try:        
        # -> Consulta para obtener los horarios ocupados en la fecha seleccionada
        cone.cursor.execute(sql, (fecha,))
        resultados = cone.cursor.fetchall()  # Obtiene todos los horarios ocupados
        
        # -> Convierte los resultados en una lista de horarios
        horarios_ocupados = [fila[0] for fila in resultados]
        
        cone.conexion.close()
        
        return horarios_ocupados    
    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")
        return []
#------------------------------------------
def obtener_id_profesional(nombre, apellido):  # -> obtiene el ID del profesional según su nombre y apellido
    cone = Conexion()
    sql = """SELECT ID_PROFESIONAL FROM profesionales WHERE NOMBRE = ? AND APELLIDO = ?"""
    
    try:
        cone.cursor.execute(sql, (nombre, apellido))  # ->  Ejecuta la consulta con los parámetros de nombre y apellido
        resultado = cone.cursor.fetchone()
        
        if resultado:  # -> Si encuentra un resultado, devuelve el ID
            return resultado[0]
        else:
            return None  # ->  Si no se encuentra, devuelve None 
    
    except sqlite3.Error as e:
        print("Error al obtener el ID del profesional:", e)
        return None 
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def obtener_nombre_apellido_profesional(id_profesional):   # -> obtiene nombre y apellido del profesional por su ID
    cone = Conexion()
    sql = """SELECT NOMBRE, APELLIDO FROM profesionales WHERE ID_PROFESIONAL = ?"""
    
    try:
        cone.cursor.execute(sql, (id_profesional,))
        resultado= cone.cursor.fetchone()
        
        if resultado:
            return resultado[0], resultado[1]  # Devuelve nombre y apellido
        else:
            return None, None  # Si no encuentra, retorna None, None
    
    except sqlite3.Error as e:
        print("Error al obtener el nombre y apellido del profesional:", e)
        return None, None
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def turno_ocupado_para_profesional(id_profesional, fecha, horario):
    cone = Conexion()  
    sql = """SELECT COUNT(*) FROM turnos 
             WHERE id_profesional = ? AND fecha = ? AND horario = ?"""
    
    try:
        cone.cursor.execute(sql, (id_profesional, fecha, horario))
        resultado = cone.cursor.fetchone()
        if resultado[0] > 0:  # ->  Si la cantidad de turnos reservados es mayor que 0, significa que ya está ocupado
            return True
        return False
    except sqlite3.Error as e:
        print("Error al verificar turno ocupado para el profesional:", e)
        return True  # -> Asume que está ocupado en caso de error
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def guardar_turno_en_bd(dni, fecha, horario, id_profesional):
    cone = Conexion()

    # -> Verifica si el turno ya está ocupado
    sql_verificar = """SELECT COUNT(*) FROM turnos WHERE FECHA = ? AND HORARIO = ?"""
    sql_insertar = """INSERT INTO turnos (DNI, FECHA, HORARIO, ID_PROFESIONAL) VALUES (?, ?, ?, ?)"""
    
    try:
        cone.cursor.execute(sql_verificar, (fecha, horario))
        resultado = cone.cursor.fetchone()
        if resultado[0] > 0:
            messagebox.showwarning("Turno Ocupado", "El turno en esa fecha y horario ya está ocupado. Elija otro.")
            return False  # -> No se puede reservar el turno
        
        # -> Si el turno está disponible, lo guarda en la base de datos
        cone.cursor.execute(sql_insertar, (dni, fecha, horario, id_profesional))
        cone.conexion.commit()
        return True  # -> Retorna True si la inserción fue exitosa
      
    except sqlite3.Error as e:
        print("Error al guardar el turno:", e)
        return False
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def obtener_turnos_por_dni(dni):
    cone = Conexion()
    sql = "SELECT FECHA, HORARIO FROM turnos WHERE DNI = ? ORDER BY FECHA, HORARIO"

    try:
        cone.cursor.execute(sql, (dni,))
        turnos = cone.cursor.fetchall()  # -> Lista de tuplas con (fecha, horario)
        return turnos
    except sqlite3.Error as e:
        print("Error al obtener los turnos:", e)
        return []
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def obtener_turnos_por_fecha(fecha):
    cone = Conexion()
    sql = """
                SELECT t.HORARIO, p.NOMBRE, p.APELLIDO, 
                       prof.NOMBRE AS PROFESIONAL_NOMBRE, prof.APELLIDO AS PROFESIONAL_APELLIDO
                FROM turnos t
                JOIN pacientes p ON t.DNI = p.DNI
                JOIN profesionales prof ON t.ID_PROFESIONAL = prof.ID_PROFESIONAL
                WHERE t.FECHA = ?
                ORDER BY t.HORARIO              
          """   
    try:
        cone.cursor.execute(sql, (fecha,))
        turnos = cone.cursor.fetchall()  # -> Lista de tuplas con (fecha, horario, nombre, apellido)
        return turnos
    except sqlite3.Error as e:
        print("Error al obtener los turnos:", e)
        return []
    finally:
        cone.cerrar_conexion()
#------------------------------------------
class Profesional():
    def __init__(self, nombre, apellido, dni, cel, mail, especialidad):
        self.id_profesional = None
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cel = cel
        self.mail = mail
        self.especialidad = especialidad

    def __str__(self):
        return f'Profesional[{self.nombre}, {self.apellido}, {self.dni}, {self.cel}, {self.mail}, {self.especialidad}]'
#------------------------------------------
def guardar_profesional(profesional):
    cone = Conexion()

    sql= f'''
             INSERT INTO profesionales (NOMBRE, APELLIDO, DNI, CEL, MAIL, ESPECIALIDAD)
             VALUES('{profesional.nombre}','{profesional.apellido}','{profesional.dni}','{profesional.cel}','{profesional.mail}', '{profesional.especialidad}')
        '''
    try:
        cone.cursor.execute(sql)
    except  Exception as e:
        print(f"Error al guardar profesional: {e}")  # Mostrar error en consola
    finally:
        cone.cerrar_conexion()
#------------------------------------------
def listar_profesionales():
    cone = Conexion()
    listar_profesionales = []
   
    sql = f'''
            SELECT * FROM profesionales as p
           
          '''
    try:
        cone.cursor.execute(sql)
        listar_profesionales = cone.cursor.fetchall()

        return listar_profesionales
    except  Exception as e:
        print(f"Error al listar: {e}")  # Mostrar error en consola
    finally:
       cone.cerrar_conexion()
#------------------------------------------
def editar_profesional(profesional, id):
    cone = Conexion()

    sql= f"""
            UPDATE profesionales
            SET NOMBRE = ?,
            APELLIDO = ?,
            DNI = ?,
            CEL = ?,
            MAIL = ?,
            ESPECIALIDAD = ?
            WHERE ID_PROFESIONAL = ?;
        """
    try:
        cone.cursor.execute(sql, (profesional.nombre, profesional.apellido,profesional.dni, profesional.cel,profesional.mail, profesional.especialidad,id))
        cone.cerrar_conexion()
        # cone.cursor.commit()
    except  Exception as e:
        print(f"Error al editar profesional: {e}")  # Mostrar error en consola
#------------------------------------------
def borrar_profesional(id):
    cone = Conexion()

    sql= f'''
         DELETE FROM profesionales WHERE ID_PROFESIONAL = {id};
         '''
    try:
        cone.cursor.execute(sql)
    except  Exception as e:
        print(f"Error al borrar profesional: {e}")  # Mostrar error en consola
    finally:
        cone.cerrar_conexion()
#------------------------------------------
class Producto():
    def __init__(self,codigo, nombre, precio,cantidad):
        self.id_producto = None
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        

    def __str__(self):
        return f'Producto[{self.codigo}, {self.nombre}, {self.precio}, {self.cantidad}]'
#------------------------------------------
def guardar_producto(producto):
    cone = Conexion()

    sql= f'''
             INSERT INTO productos (Codigo, Nombre, Precio, Cantidad)
             VALUES('{producto.codigo}','{producto.nombre}','{producto.precio}','{producto.cantidad}');
        '''
    try:
        cone.cursor.execute(sql)
    except  Exception as e:
        print(f"Error al guardar producto: {e}")  # Mostrar error en consola
    finally:
        cone.cerrar_conexion()
#------------------------------------------
#------------------------------------------
