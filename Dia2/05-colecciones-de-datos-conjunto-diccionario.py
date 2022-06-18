# Conjunto (Set
# Coleccion de datos desordenada (no lleva orden en los indices)

meses = {'enero', 'febrero', 'marzo', 'abril'}
print(meses)
print('enero' in meses)
print('agosto' in meses)

meses.add('mayo')
meses.add('junio')

print(meses)

# tbn se puede agregar un conjunto de nuevos elementos 
meses.update(['julio', 'agosto', 'septiembre', 'junio','julio' ])
print(meses)

# el metodo discard o remove elimina todos los valores que coinsidan con ese contenido 
meses.discard('junio')
print(meses)

meses.remove('julio')
print(meses)

