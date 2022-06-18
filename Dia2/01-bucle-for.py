# Bucle: se repite y repite y repite lo mismo 
numeros = [10,20,30,40,50,60]

for numero in numeros: 
    print(numero)

frase_motivadora = 'Al madruga, encuentra todo cerrado'

# contador o flag bandera
contador = 0
for caracter in frase_motivadora:
    # print (carcater)
    # Cuentame cuantas letras n hay en esa frase >2
    if caracter == 'n':
        print ('hay una n')
        # contador = contador +1
        contador += 1
print ("hay {} veces repetidas la letra n".format(contador))

#--------------------------------------
# RANGE permite establecer parametros.

for valor in range (10):
    # range me permite pasar un parametro, dos parametros 

    print(valor)

for valor in range (3,7):
    # empezar desde el numero 0 hasta < 10 y se incrementa de uno en uno 
    print(valor)

for valor in range(4,7,2):
    # el primer valor parametro sera el numero en el cual va ha empezar y el segundo hasta que numero debe llegar y el tercer parametro  sera de cuanto en cuanto debe alterar en contador 
    print(valor)

# EJERCICIOS 2
# Cuantos de esos numeros son pares y cuantos son multiples de tres / usar un for con pistas condicionales 
numeros = [10,30,12,17,24,67]

contador_numero_pares = 0 
contador_multiplos_tres = 0

for numero in numeros:
    if numero % 2 == 0:
        contador_numero_pares += 1
    
    if numero % 3 == 0:
        contador_multiplos_tres += 1 

print ("Hay {} numeros pares y hay {} multiplos de tres".format(contador_numero_pares, contador_multiplos_tres))

#------------------------------------------
# BREAK: sirve para finalizar de manera prematura un boucle (for, while)
#  supongamos que los 10000 son los usuarios es un sistema y queremos encontarar al usuario con un determinado nombre (y ese usuario es el numero 600)
for valor in range(0,10000):
    print(valor)
    if (valor == 600):
        print('el usuarios fue encontrado')
        # break > sirve para finalizar de manaera prematura un bucle ( for, while)
        break 

#-------------------------
#CONTINUE: sirve para que el codigo que viene a continuacion se no ejecuta.
for valor in range(0,20):
    if (valor == 5):
        print('el usuarios fue encontrado')
        continue
    print(valor)

#-----------------------------
for valor in range(0,20):
    # TODO: implementar la logica 
    # pass > no hara nada pero evitara que nos lance error python
    pass

#----------------------------

alumnos = ['EDUARDO', 'LILY', 'JOSE', 'RAFAEL']

for alumno in alumnos:
    if alumno == 'LUIS':
        print(alumno)
else:
    # Ingresara una vez que haya terminado de iterar el for 
    print('No se encontro el alumno a buscar')