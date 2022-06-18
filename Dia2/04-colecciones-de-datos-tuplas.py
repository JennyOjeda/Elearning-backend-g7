# tuplas son colecciones de datos ordenadas PERO no editables
profesores = ('EDUARDO', 'OSMAR')
print(profesores[0])

# profesores[0] = 'XIMENA'
# profesores.append('RAUL')

data = (1, True, 'JUNIO', 14.5 ,[1,2,3,4])
print(data[1:4])

# se puede eliminar toda la variable pero no se puede eliminar parte del contenido de la tupla
del data 

notas = (10,15,15,18,10,5,7,14)
print(notas.count(10))
print(notas.count(20))
print(notas.count('Onomatopeya'))

# index > si existe ese valor en la tupla me retornara la posición en la que se encuentra, sino existe emitira un error
print(notas.index(15))
