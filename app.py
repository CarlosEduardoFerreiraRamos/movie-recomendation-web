from flask import Flask
from flask_restful import Resource, Api
from flask_socketio import SocketIO, emit

from resources import HelloWorld, Movie

app = Flask(__name__)

api = Api(app)
api.add_resource(HelloWorld, '/')
api.add_resource(Movie, '/movie/<string:title>')

socketio = SocketIO(app)

@socketio.on('predict')
def predict(value):
    print('in connect socketio predict', value)
    emit('predict', 'through predict')

@socketio.on('connect')
def connect():
    print('in connect socketio ws')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app,debug=True)