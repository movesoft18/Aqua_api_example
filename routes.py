from controllers.say_hello import SayHello
from controllers.server_version import ServerVersion
from controllers.device_state import DeviceState
from app_data.definitions import mysql_connection

def InitRoutes(api):
    additional_params = {
        'connection': mysql_connection,
    }
    
    api.add_resource(SayHello, '/api/v1/hello')
    api.add_resource(ServerVersion, '/api/v1/version')
    api.add_resource(DeviceState, '/api/v1/status',
                     resource_class_kwarg=additional_params)