# crear una clase persona en la cual se guarda su nombre, fecha_nacimiento, nacionalidad, dni, además también una clase alumno y una clase docente en la cual el alumnos, a diferencia del docente tenga una serie de cursos matriculados, y el docente por su parte tenga un número del seguro social y su cuenta de la CTS. En base a los visto de herencia crear las clases y además ver algun atributo o metodo que deba ser privado. 

class Persona:
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
        self.nombre = nombre 
        self.nacionalidad = nacionalidad
        self.dni = dni 
        self.fecha_nacimiento = fecha_nacimiento

    def Info(self):
        return {
            "DNI":self.dni,
            "Fecha de nacimiento":self.fecha_nacimiento,
            "Nombre":self.nombre,
            "Nacionalidad":self.nacionalidad,
        }

class estudiante(Persona):    
    def __init__(self,curso,nombre,fecha_nacimiento,nacionalidad,dni ):
        self.curso = curso
        Persona.__init__(self,nombre,fecha_nacimiento,nacionalidad,dni)
        

    def info(self):      
        estudiante ={
                    "Nombre":self.name,
                    "Curso":self.curso,              
                    "Nacionalidad":self.nacionalidad, 
                }
        for k, v in estudiante.items():
            print(f"{k}: {v}")

    def privateInfo(self):
        # private info 
        privateInfo = super().privateInfo()

        print("Información Personal")   
        for k, v in privateInfo.items():
            print(f"{k}: {v}")

class Profesor(Persona):
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni,cts,seguro_social):
        self.seguro = seguro_social
        self.cts= cts
        super().__init__(nombre,fecha_nacimiento,nacionalidad,dni)

    def info(self):
        print(            
                "Nombre:",self.nombre,"\n"
                "Nacionalidad:",self.nacionalidad,          
        )

    def privateInfo(self):
        privateInfo = super().privateInfo()

        print("Información Personal")        
        print("DNI:",privateInfo["DNI"])
        print("Cumpleaños:",privateInfo["Fecha de nacimiento"])
        print("Cuenta CTS:",self.cts)
        print("Seguro Social:",self.seguro_social)



print("Estudiante")
estudiante1 = estudiante("Comunicacion","Pedro","2009-04-18","Perú","123456789")
estudiante1.info()
estudiante1.privateInfo()
print()

print("Profesor")
profesor1 = Profesor("12-ad","123-da","Alejandro","1990-02-22","Perú","232452345" )
profesor1.info()
profesor1.privateInfo()