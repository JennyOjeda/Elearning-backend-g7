# PILARES 
# 1.ABSTRACCION(abtraer las prpiedades con mayor detalles, abstraer a los mas minimo)
# 2.ENCAPSULAMIENTO ()
# 3.HERENCIA
# 4.POLIFORMISMO

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
        # si queremos indicar que un atributo de la clase va ha ser privada(no va apoder ser accedida desde fuera de la clase) tendremos que colocar doble guion bajo al incio nombre del atributo 
        self.__serie = marca + modelo
        # TODO: explicar el tipo PROTECTED
        self._serie2 = marca + modelo

    def mostrarSerie(self):
        print(self.__serie)

auto = Vehiculo('kIa','picanto')
camion = Vehiculo('volvo', 'F30')
print(auto.marca)
print(auto._serie2)
auto.mostrarSerie()
