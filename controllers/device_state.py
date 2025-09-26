from flask_restful import Resource, reqparse
from app_data.devices_data import get_device_data, set_device_data

class DeviceState(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'deviceId',
            type=int,
            location='args',
            required=True,
            )
        args = parser.parse_args()
        state = get_device_data(args['deviceId'])
        if state is None:
            return {
                'error': 5,
                'message': 'Объект, указанный в запросе, не найден',
                'data': None,
            }, 200
        else:
            return {
                'error': 0,
                'message': 'Ok',
                'data': state
            }, 200            
    
    def post(self):
        pass