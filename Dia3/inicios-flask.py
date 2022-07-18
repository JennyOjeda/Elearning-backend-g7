from flask import Flask, request
from datetime import datetime

from flask_cors import CORS


# creamos instancias 
# __name__ > variable propia de python que muestra que el archivo que estamos utilizando es el archivo principal del proyecto, sis es el archivo principal su valor esa '__main__' caso contrario indicara otro valor
app = Flask(__name__)

# la clase CORS si solamente le pasamos la instancia de nuestra clase flask entonces modificara los CORS para que puedan ser accedidos por todo el mundo(cualquier origen, cualquier metodo, cualquier cabecera)
CORS(app)

productos = []
# Enpoints
# Decorador es un patron de software que se utiliza para modificar el comortamiento de un metodo de una clase sin la necesidad de emplear otros metodos como la herencia ademas tampoco es necesario modificar el comportameinto del metodo de dicha clase.
@app.route('/')
def rutaInicial():
    print('ingreso al enpoint inicial')
    return 'Bienbenido a tu primer API de Codigo de Backend'

@app.route('/estado')
def estadoAPI():
    return{
        'hora': datetime.now().strftime('%Y-%m-%d  %H-%M-%S') # string from time 
    }

@app.route('/producto', methods=['POST'])
def gestionProductos():
    # get_json() > convierte el json que el cliente envia a un diccionario para que python lo pueda entender
    print(request.get_json())
    producto = request.get_json()
    productos.append(producto)
    return {
        'message': 'Producto creado exitosamente',
        'content': producto
    }


@app.route('/devolver-productos', methods=['GET'])
def devolverProductos():
    return {
        'message': 'Los productos son',
        'content': productos
    }
# levantamos nuestro servidor para que se quede a la espera de posibles peticiones durante un tiempo determinado
# debug > inidicara que estamoms en un servidor de prueba entonces cada vez que hagamos algun cambio a algun archivo del proyecto automaticamente se reiniciara el servidos agregando los nuevos cambios (su valor por defecto es falso)
app.run(debug=True)