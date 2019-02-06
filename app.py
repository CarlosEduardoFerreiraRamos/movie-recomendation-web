from flask import Flask
from flask_restful import Resource, Api
from resources import HelloWorld, Movie

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(Movie, '/movie/<title>')

if __name__ == '__main__':
    app.run(debug=True)