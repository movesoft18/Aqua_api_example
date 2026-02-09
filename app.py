from flask import Flask
from flask_restful import Api
from routes import InitRoutes
from os import environ
from app_data.definitions import server_port
from flask_session import Session
import os


app = Flask(__name__)
api = Api(app)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
InitRoutes(api)

app.config['APP_PATH'] = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = app.config['APP_PATH'] + os.sep + 'dbimages'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 100

if __name__ == '__main__':
    HOST = '192.168.110.129'#environ.get('SERVER_HOST','localhost')
    PORT = server_port
    app.run(HOST, PORT, debug=True)
    
    # http://localhost:5001/api/v1/hello
    # http://localhost:5001/api/v1/status?deviceId=2