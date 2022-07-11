from flask import Flask

# creamos instancias 
# __name__ > variable propia de python que muestra que el archivo que estamos utilizando es el archivo principal del proyecto, sis es el archivo principal su valor esa '__main__' caso contrario indicara otro valor
app = Flask(__name__)

# Enpoints
# Decorador es un patron de software que se utiliza para modificar el comortamiento de un metodo de una clase sin la necesidad de emplear otros metodos como la herencia ademas tampoco es necesario modificar el comportameinto del metodo de dicha clase.
@app.route('/')
def rutaInicial():
    print('ingreso al enpoint inicial')
    return 'Bienbenido a tu primer API de Codigo de Backend'

# levantamos nuestro servidor para que se quede a la espera de posibles peticiones durante un tiempo determinado
# debug > inidicara que estamoms en un servidor de prueba entonces cada vez que hagamos algun cambio a algun archivo del proyecto automaticamente se reiniciara el servidos agregando los nuevos cambios (su valor por defecto es falso)
app.run(debug=True)