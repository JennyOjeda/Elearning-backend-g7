edad_roberta = 20 

if edad_roberta >= 18 :
    print('Si puede ingresar a la discoteca')
else:
    print('No puedes entrar, anada al cine')

# ----------------------------
edad_martin = 70

if edad_martin >= 65:
    print('Esa persona esta jubilada')
elif edad_martin >= 18:
    print('Esa persona es mayor de edad')
elif edad_martin >= 0:
    print('Esa persona es mejor de edad')
else: 
    print ('Edad imposible')

# ------------------------------------
# pasar valores con el input, la forma paraingresar valores al programa desde consola 
# data = input("Hola, ingresa tu nombre:   ")
data = input("Hola, ingresa tu talla de polo")
print(type(data))

# Dependiendo de la talla del polo podriamos hacer lo siguiente: indicar que llegara para fines de mes, si es L o M solicitar el color del polo, si es S indicar que solamente hayun color Morado, si ingresa otra cosa, indicar que la talla es incorrecta 

talla = input("Hola, ingresa tu talla de polo").lower(),
print(type(talla))
if talla == 'xl':
    print('El polo llegara a fin de mes')
elif talla  == 'L':
    print('Ingresa el color del polo ')
elif talla =='S':
    print('Solo hay color morado')
else: 
    print ('Talla correcta ')




