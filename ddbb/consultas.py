from .conexion import Conexion
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
              NOMBRE TEXT NOT NULL
              );

              CREATE TABLE IF NOT EXISTS productos
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
              NOMBRE TEXT NOT NULL        
             
              );

           """
    try:
        cone.cursor.executescript(sql)
    except:
        pass
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


# def listar_pacientes_por_dni(dni):
#     cone = Conexion()  # Conectar a la base de datos

#     sql = ("SELECT nombre, apellido, dni, celular, email FROM pacientes WHERE dni = ?", (dni,))

#     
#     cone.cursor.execute(sql) # Consulta la bd para obtener los datos del paciente por DNI
#     paciente = cone.cursor.fetchone()  # Obtener el primer resultado encontrado

#     cone.cerrar_conexion() # Cerrar la conexión a la base de datos

#     return paciente  # Retorna una tupla con los datos o None si no encuentra el paciente
