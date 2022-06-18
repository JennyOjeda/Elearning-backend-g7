# while 
numero = 10 
# es un bucle que se realizara de manera automaica hasta que la condicion o condiciones dejen de ser verdaderas

while numero > 0: 
    print('Numero positivo')
    print(numero)
    numero -= 1

# do while > no existe en python

#--------------------------------  
# solicitar 5 digitos para la loteria pero estos  no pueden ser mayor que 100 ni numero negativos. 
# pedimos al usuario que ingrese un valor utilizando input

contador_numeros = 1
while contador_numeros < 6:
    numero = int(input('Ingresa el numero de la loteria: '))
    if not(numero > 100 or numero < 0):
        contador_numeros +=1
        continue
    print('Numero ingresado es invalido, vuelva a intentar')

#----------------------------------
while contador_numeros < 6:
    numero = int(input('Ingresa el numero de la loteria: '))
    if not(numero < 100 and numero > 0):
        contador_numeros +=1
        continue
    print('Numero ingresado es invalido, vuelva a intentar')