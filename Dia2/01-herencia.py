class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Alumno(Usuario):
    def __init__(self, Nombre, apellido2, anio, seccion):
        self.anio = anio
        self.seccion = seccion
        # es un metodo que sirve para utilizar los metodos y atributos 
        # y ya con esto he llamado a mi constructor PERO del padre
        super().__init__(nombre= Nombre, apellido= apellido2)

    def info(self):
        infoUsuario = super().info()
        data= {
            'anio': self.anio,
            'seccion': self.seccion,
        }
        # const x= {nombre: 'eduardo', 'dia': 'jueves}
        # const {nombre} = x
        # const y = {...x}
        # En python para hacer destructuracion de un diccionario se realiza de la siguiente manera 

        return{**data, **infoUsuario}
        
alumnoEduardo = Alumno('Eduardo', 'de Rivero', 'Sexto', 'A')

usuarioRaul = Usuario('Raul', 'Mendoza')

informacion = alumnoEduardo.info()
print(informacion)
print(usuarioRaul.info())
