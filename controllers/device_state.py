from flask_restful import Resource, reqparse
from app_data.devices_data import get_device_data, set_device_data, serialize_all

class DeviceState(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'deviceId',
            type=int,
            location='args',
            required=False,
            )
        args = parser.parse_args()
        if args['deviceId'] is None:
            return {
                'error': 0,
                'message': 'Ok',
                'data': serialize_all()                
            }
        
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
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            'deviceId',
            type=int,
            location='json',
            required=True,
            )
        parser.add_argument(
            'value',
            type=int,
            location='json',
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
        if state['type'] == 'sensor':
            return {
                'error': 7,
                'message': 'Невозможно изменить состояние данного устройства',
                'data': None,
            }, 200            
        if state['status'] != args['value']:
            set_device_data(args['deviceId'], args['value'])
            state['status'] = args['value']
        return {
            'error': 0,
            'message': 'Ok',
            'data': state
        }, 200              