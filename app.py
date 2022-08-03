from flask import Flask
from config import conexion
from models.participante import Participante
from dotenv import load_dotenv
# el METODO load_dotenv carga todas las variables 

# Me devuelve todas las variables en forma de diccionario
from os import environ

# Carga todas las variables declaradas en el archivo .env como variable de entorno para que puedan ser acreditados desde el metodo 'environ'

load_dotenv()

app = Flask(__name__)
#URI dialecto://usuario:password@host:puerto/base_de_dato
#     'mysql://root:root123@localhost:3306/concierto'
app.config['SQLALCHEMY_DATABASE_URI']=environ['DATABASE_URL']
# sqlalchemy hace un seguimiento a las modificaciones que haremos a la bd pero actualmente tiene un valor determinado PERO en futuros version tendremos que  OBLIGATORIAMENTE indicar si queremos hacer el seguimiento o no 

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 
# inicializado mi conexion de mi sqlalchemy con la base de datos pero todabia no me he conectado
conexion.init_app(app)

# se ejecuta la conexion y se crearan las tablas pero sinohay ninguna tabla a crear entonces no lanzara error de credenciales invalidas
conexion.create_all(app=app)

# como es el archivo principal  utilizamos el nombre "main" no se recomienda tener varios instancias 

if __name__ == '__main__':
    app.run(debug=True)