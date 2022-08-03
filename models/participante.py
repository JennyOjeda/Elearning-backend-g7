from config import conexion
from sqlalchemy import Column,types


class Participante(conexion.Model):
    #ahora esta clase tendra un comprtamiento en forma de una tabla en la base de datos (todos los atributos que declare que sea propio de la base de datos se creara como columna)
    # conexion.Column() === column()
    # Documentacion > https://docs.sqlalchemy.org/en/14/core/metadata.html?highlight=column#sqlalchemy.schema.Column.__init__
    # cuando utilizamos un tipo de datos en mayuscula este tipo de datos es especifico para un determinado motor de base de datos ya que no es lo mismo el uso de las mayusculas y minusculas ejmplo: boolean, BOOLEAN.

    # id INT PRIMARY_KEY AUTO_INCREMENT
    id = Column(type_= types.Integer, autoincrement=True, primary_key=True)
    # nombre VARCHAR(50) NOT NULL
    nombre = Column(type_=types.String(50), nullable=False)
    apellido = Column(type_=types.String(50), nullable=False)
    telefono = Column(type_=types.String(10))
    password = Column(type_=types.Text, nullable=False)
    zona = Column(type_=types.Enum('SUPER_VIP','VIP','GENERAL'),
                  default='GENERAL', nullable=False)
    comentario = Column(type_=types.Text)
    correo = Column(type_=types.String(45), nullable=False)

    # se modifica el nombre de la tabla a a nivel de base de datos para que no se llame igual que la clase(en singular y con la primera en mayuscula)
    __tablename__='participantes'
 