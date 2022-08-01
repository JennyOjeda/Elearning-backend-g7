from flask import Flask
from config import conexion

app = Flask(__name__)


# inicializado mi conexion de mi sqlalchemy con la base de datos pero todabia no me he conectado
conexion.init_app(app)

# se ejecuta la conexion y se crearan las tablas pero sinohay ninguna tabla a crear entonces no lanzara error de credenciales invalidas
conexion.create_all(app=app)




# como es el archivo principal  utilizamos el nombre "main" no se recomienda tener varios instancias 

if __name__ == '__main__':
    app.run(debug=True)