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