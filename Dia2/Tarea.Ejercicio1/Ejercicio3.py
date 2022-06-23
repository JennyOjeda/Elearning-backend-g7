# EJERCICIO 4 
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *

# SOLUCION:
n = 4
# triangulo de de 90 grados normal  
for i in range(1, n + 1): 
    for j in range(i):
        print('*', end='')
    print()

# tringulo investido 

for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()