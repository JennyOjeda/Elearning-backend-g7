from camelcase import CamelCase

camelcase = CamelCase(__name__)

parrafo = 'hola amigos vamos si esta libreria funciona'

resultado = camelcase.hump(parrafo)
print(resultado)