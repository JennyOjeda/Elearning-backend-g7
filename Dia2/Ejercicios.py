# EJERCICIO 1
# Ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
# for numero in range(5):
#     print(numero, end="")

#-------------------------------------
# EJERCICIO 2
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# SOLUCION: 

# m = int(input("Numero de columnas: "))
# n = int(input("Numero de filas: "))

# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         print("*", end="")
#     print("  ")

#-------------------------------------
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
#-------------------------------------
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

#--------------------------------------------
# EJERCICIO 5
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12

# SOLUCION: 

def collatz(num):
    sec = [num]
    while num > 1:
        if num % 2 == 0:
            num //= 2 
        else:
            num = num * 3 + 1 
            sec.append(num)
        
        return sec

secuencia = collatz(11)

for i in secuencia:
    print (i, end=" ")


#----------------------------------------------------------
# EJERCICIO 6
# si el texto de ingreso es:
# texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
# resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]
# Hacer el codigo para ello

# SOLUCION:
text = input("Ingresar el texto: ")
lista = text.split(" ")
print([" , ".join(lista)])

#---------------------------------------------------------
# EJERCICIO 7
# ingresar numeros hasta que ese numero sea adivinado
# numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'

# SOLUCION 
num_ad=int(input("ingrese numero ah adivinar: "))
num=10
while num_ad!=num:
    if num_ad<num:
       print("el numero es mayor que ese")
    elif num_ad>num:
        print("el numero es menor que ese")
    num_ad=int(input("ingrese numero ah adivinar: "))
print("felicitaciones adividaste el numero")

#----------------------------------------------------------

# EJERCICIO 8
# dado los siguientes numeros:
# numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1

numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
m_tres=0
m_cinco=0
for i in numeros:
    if i%3==0 and i%5==0:
        continue
    elif i%3==0:
        m_tres+=1
    elif i%5==0:
        m_cinco+=1
print("los multiplos de 3 son: {} y los multiplos de 5 son: {}" .format(m_tres,m_cinco))
