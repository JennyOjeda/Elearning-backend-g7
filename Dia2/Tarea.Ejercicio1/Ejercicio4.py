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