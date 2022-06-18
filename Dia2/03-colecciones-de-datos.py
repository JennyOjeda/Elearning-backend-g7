# LISTAS: agregar y quitar elementos
alumnos = ['JAVIER', 'aLEJANDRO', 'ALEXANDRA', 'JENNY']
otra = [1,10,'hola',True, 5.2, None]

# Son coleccciones de datos ordenadas (posiciones), las posiciones siempre empiean en 0

print(alumnos[0])
# si queremos acceder a una posisicon que no existe en nuestra lista nos emitira un error, a diferencia de JS que se muestra 'undefine'
# print(alumnos[0])

variados = [10, [1,2,3]]
print(variados[1][1])

# cuando usamos dos puntos ":" al momento de definir la posisicon de una lista entonces le estaremos indicando que queremos una sublista de esa lista siendo el primer valor la posicion inical y el segundo valor hasta que posision tiene que llegar (menor que)

print(alumnos[1:3])
# destrcturas de una  (extraer los elementos internos de la lista)
print(alumnos[:])
#  entonces la invierte, es decir ahora la posicion -1 sera el ultimo elemento  delas listas y asi susesivamente 
print(alumnos[-1])
print(alumnos[-2])

for alumno in alumnos:
    if alumno == 'EDUARDO':
        print('SI ESTA')
        break
# Sentido de pertenencia > podemos consultar si un vaalor determinado existe una lista 
print ('EDUARDO' in alumno)
print(10 in alumnos)

# listas son colecciones de datos EDITABLES
alumnos[0] = 'MARTIN'
print(alumnos)

# append > sirve para agregar un valor a la lista final 
alumnos.append('IVANOV')
print(alumnos)

# extend > combinar las listas en una sola lista
alumnos.extend(['LUIS', 'LILY','JORDAN'])
print(alumnos)

# otra forma de combinar es concatenando las listas
alumnos += ['YORDY','JAVIER','RUBEN']
print(alumnos)

# Eliminar un elemento de la lista 
del alumnos[1:3]
print(alumnos)

# segunda forma usando el metodo pop, este metodo lo que hace es eliminar elcontenido de esa posicion PEERO se puede almacenar el contenido de otra variable.
alumno_eliminado = alumnos.pop(2)

print(alumnos)
print(alumno_eliminado)

# Tercer forma usada el metodo clear limpiaremos toda la lista y la dejaremos en blanco
alumno.clear()
print(alumnos)









