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
