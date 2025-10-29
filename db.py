"""
def crea_csv(nombre_archivo, columnas):
    file = open(nombre_archivo, "wt")
    csv_line = ",".join(columnas) + "\n"
    file.writelines([csv_line])
    file.close()


def agrega_valores_csv(nombre_archivo):
    file = open(nombre_archivo, "at")
    nombre = input("Ingrese nombre: ")
    while nombre != "":
        apellido = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        vector = [nombre, apellido, dni]
        fila = ",".join(vector) + "\n"
        file.writelines([fila])
        nombre = input("Ingrese nombre: ")
    file.close()

agrega_valores_csv("db.csv")
"""

# CLASE PRESENCIAL

class Transforma(object):
    def __init__(self,atributos):
        self.keys = atributos

    def toDict(self,values):
        if len(values) != len(self.keys):
            return None
        d = {}
        i = 0
        while i < len(values):
            d[self.keys[i]] = values[i]
            i = i + 1
        return d

class DB(object):
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        db = []
        file = open(self.filename, "rt")
        line = file.readline() # Leo encabezado

        if line == "":
            return db
        keys = line.split(",")
        tran = Transforma(keys)
        line = file.readline() # Leo la primera linea
        while line != "":
            values = line.split(",")
            d = tran.toDict(values)
            db.append(d)
            line = file.readline()
        file.close()
        return db

    def write(self, registros):
        pass


db = DB("db.csv")
registros = db.read()
i = 0
while i < len(registros):
    print("Nombre: ", registros[i]["nombre"])
    i = i + 1