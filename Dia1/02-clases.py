# PROGRAMACION ORIENTADA A OBJETOS (POO) OOPS 
# Una clase es como una plantilla que va a ser pata empezar a definir los atributos y metodos de ese determinado objeto

class Persona:
    # atributos 
    estatura = 100
    colorOjos = 'cafe'
    colorCabello = 'Negro'
    fechaNacimiento = '2000-01-01'

    def saludar(self):
        print('Hola buenos dias')

# cuando creamosun copia de una plantilla se le dice "instanciar" o crear una referencia de una clase

personaEduardo = Persona()
print(personaEduardo.colorCabello)

#CONSTRUCTOR 
# self > es la referencia de la instancia que hemos creado en relacion a su posicion de memoria, con esto no modificaremos a las demas instancias cuando cambiemos algun atributo o comportamiento de una instancia
# self debe de ser dclarada como primer parametro de TODO metodo de una clase OBLIGATORIAMENTE

class Mascota:
    def __init__(self, nombre, especie, raza, sexo):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.sexo = sexo

    def info(self):
        print(self.nombre)
        print(self.especie)
        print(self.raza)
        print(self.sexo)

mascotaPerro = Mascota('Morocha','Perro','Salchicha','Femenino')
MascotaGato = Mascota('Michifus','Gato', 'siames','masculino')