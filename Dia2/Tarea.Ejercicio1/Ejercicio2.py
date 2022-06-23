# EJERCICIO 3
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****

# SOLUCION 
n =5
for i in range(n): 
    print(' ' * (n -i -1)+ '*' *(2 * i +5))

for i in range(n):
        # print('*', end='')
    for i in range(1, n + 1):
        print('*', end='')
    print()

for y in range(n,0,-1):
    for j in range((n+1)-y-1):
        print (' ',end="")
    for k in range(((n-2)+y*2)):
        print ('*',end=""),
    if y==n:
        for k in range(n-2,0,-1):
            print()
            print ('*'*((n-2)+y*2),end="")  
    print()