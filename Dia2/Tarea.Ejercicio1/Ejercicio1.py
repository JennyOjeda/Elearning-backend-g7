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

m = int(input("Numero de columnas: "))
n = int(input("Numero de filas: "))

for i in range(1, m + 1):
    for j in range(1, n + 1):
        print("*", end="")
    print("  ")