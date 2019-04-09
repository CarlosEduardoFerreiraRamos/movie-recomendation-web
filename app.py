'''libs'''
from flask import Flask
from celery import Celery
from flask_restful import Resource, Api
from flask_socketio import SocketIO, emit
'''internal'''
from resources import HelloWorld, Movie
from tasks import Tasks

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] ='redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND']='redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
tasks = Tasks(celery)
tasks.create_tasks()

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