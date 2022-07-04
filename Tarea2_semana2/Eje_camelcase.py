def camelCase(palabras = ''):
    t = palabras.split()
    palabras= ""
    for letra in t:
           x='a'
           y='is'
           palabras+= " "+letra if letra==x or letra ==y else " "+letra.title()
    return palabras.strip()

frase = "hola amigos como estan"

print(camelCase(frase))