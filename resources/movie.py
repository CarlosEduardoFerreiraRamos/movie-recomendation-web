from flask_restful import Resource
from service import MovieRecomender as mr

class Movie(Resource):

    def __init__(self):
        self.service = mr()

    def get(self, title):
        holder = 'The Grandfather'
        if not holder == title:    
            '''recomendations = self.service.predict(title)
            print('get Method')
            print(recomendations)'''
            task_id = 0    
            return {'taskId': task_id}
        else:
            # check prediction
            # task_id = task_id
            return {'prediction': 'predicted'}