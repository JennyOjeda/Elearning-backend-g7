from flask_restful import Resource
#La clase resource se comportora como si fuese un controlador es decir que si definimos un metodo llmado get

class ParticipanteController(Resource):
    def get(self):
        return{
            'message': 'Ingreso al get'
        }