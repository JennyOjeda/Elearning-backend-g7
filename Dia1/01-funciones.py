def saludar():
    print('Buenos tardes!')

saludar()

def saludarConNombre(nombre):
    print("Holas{}, como te va?".format(nombre))

def saludoCordial(nombre):
    '''Funcion que recibe un nombre y te saluda cordialmente preguntando como te va '''
    print("Hola {}, como te va".format(nombre))

saludarConNombre('Eduardo')

saludoCordial('Eduardo')

#funcion puede devolver un valor 

def calcularIGV(valor):
    """FUNCION QUE RECIBE EL VALOR Y TE DEVULEVE L VALOR INCLUIDO"""
    valorIncluidoIGV = valor * 1.18
    return valorIncluidoIGV

precio = 100
precioConIGV = calcularIGV(precio)
print(precioConIGV)

precio = 110
precioConIGV = calcularIGV(precio)
print(precioConIGV)

precio = 800
precioConIGV = calcularIGV(precio)
print(precioConIGV)

precio = 600
precioConIGV = calcularIGV(precio)
print(precioConIGV)

def calcularSalarioMinimo(profesion, experiencia):
    salarioMinino = 1050
    if profesion == 'Desarrollador':
        if experiencia == 'Basica':
            salarioMinimo = 3000
        
        elif experiencia == 'Media':
            salarioMinimo = 4000

        elif experiencia == 'Avanzado':
            salarioMinimo = 7000

    elif profesion == 'Marketing':
        if experiencia == 'Basica':
            salarioMinimo = 2500
        
        elif experiencia == 'Basica':
            salarioMinimo = 4150   

        elif experiencia == 'Avanzada':
            salarioMinimo = 6820  
    
    return salarioMinimo

profesion, experiencia = 'Desarrollador', 'Media'
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

profesion, experiencia = 'Marketing', 'Media'
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

profesion, experiencia = 'Austronauta', 'Media'
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

# De esta manera se puede indicar a que parametro va a ir determinado valor si no queremos respetar el orden de los parametros de
salario = calcularSalarioMinimo(experiencia='Basica', profesion='Marketing')


electrodomesticos = []

def registrarElectrodomesticos(nombre, precio, alamcen='Las Malvinas'):
    electrodomesticos.append({'nombre': nombre, 'precio': precio, 'alamcen': alamcen})
    return True

registrarElectrodomesticos('licuadora 12v', 115.00)
registrarElectrodomesticos('Freidora de aire', 100, 'Cercado')
registrarElectrodomesticos('Secadora de cabello', 140)

print(electrodomesticos)

def contarElectrodomesticosPorAlmacen():
    """Cuenta cuantos electrodomesticos hay en cada almacen"""
    # usar un for para iterar los electrodomesticos 
    malvinas = 0 
    Cercado = 0
    otro = 0

    for electrodomesticos in electrodomesticos:
        if electrodomesticos['almacen'] == 'Las Malvinas':
            malvinas +=1
        elif electrodomesticos['almacen'] == 'cErcado':
            cercado += 1
        else:
            otro += 1

# luego de iterar los electrodomesticos indicar
# en las malvinas hay dos electrodomesticos y en el cercado hay un electrodomestico
    return[malvinas, cercado, otro]

resultado = contarElectrodomesticosPorAlmacen()
print('En las Malvinas hay {}, en Cercado hay {} y en otros hay{} electrodomesticos'.format(resultado[0],resultado[1], resultado[2]))

# si es una funcion queremos recibir un numero indeterminado de valores 
def recibirAlumnos(clase, *alumnos):
    # cuando un parametro tiene * al comienzo significa que ese parametro recibira n valores y lo convertira a una tupla
    # alumnos[0]= 'Juan'
    print(type(alumnos)) # mostrar el tipo de datos que contiene esta variable, typeof en Javascript
    print(alumnos) 
    alumnos_lista = list(alumnos) # se convierte de un tipo de dato a otro SIEMPRE Y CUANDO SEAN COMPATIBLES
    # alumnos_numero = int(alumnos) # esto al no ser compatible emite un error y matara al programa
    print(type(alumnos_lista))
    alumnos_lista[0] = 'Rigoberto'
    print(clase)

recibirAlumnos('Eduardo', 'Juancarlos', 'Jenny', 'Liy', 'Manunel', 'Cristian', 'Wilson', 'Alejandro')
recibirAlumnos('Eduardo','Juan Carlos', 'Lily', 'Manuel','Wilson', 'Alejandro')





