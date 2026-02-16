from controllers.get_video import VideoFeed
from controllers.say_hello import SayHello
from controllers.server_version import ServerVersion
from controllers.device_state import DeviceState
from controllers.user_data import UserData
from controllers.signin import SignIn
from controllers.signup import SignUp
from app_data.definitions import mysql_connection

def InitRoutes(api):
    additional_params = {
        'connection': mysql_connection,
    }
    
    api.add_resource(SayHello, '/api/v1/hello')
    api.add_resource(ServerVersion, '/api/v1/version')
    api.add_resource(SignIn, '/api/v1/auth', 
                     resource_class_kwargs=additional_params)
    api.add_resource(DeviceState, '/api/v1/status',
                     resource_class_kwargs=additional_params)
    api.add_resource(SignUp, '/api/v1/signup',
                     resource_class_kwargs=additional_params)    
    api.add_resource(UserData, '/api/v1/user', 
                     resource_class_kwargs=additional_params)
    api.add_resource(VideoFeed, '/api/v1/video_feed', 
                     resource_class_kwargs=additional_params)