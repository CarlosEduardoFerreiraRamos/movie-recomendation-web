from flask_restful import Resource
from service import MovieRecomender as mr

class Movie(Resource):

    def __init__(self):
        self.service = mr();

    def get(self, title):
        recomendations = self.service.predict(title)
        print('get Method')
        print(recomendations)
        return {'recomendations': recomendations}