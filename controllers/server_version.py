from flask_restful import Resource

class ServerVersion(Resource):
    def get(self):
        return {
            'error': 0,
            'message': 'Ok',
            'data': { 
                'version' : '1.0.0'
            },
        }, 200