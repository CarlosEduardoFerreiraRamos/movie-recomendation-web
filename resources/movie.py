from flask_restful import Resource

class Movie(Resource):
    def get(self):
        return {'hello': 'world'}