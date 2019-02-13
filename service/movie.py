from util import DataManager as dm

class MovieRecomender(object):
    
    def predict(self, title):
        return self.get_recommendations(title) #.head(10)

    def get_similar(self):
        return dm.get_model('model')

    def get_ref_files(self):
        return dm.get_csv('indices',index=0), dm.get_csv('titles')

    def get_recommendations(self,title):
        print('get_recommendations')
        indices, titles = self.get_ref_files()
        model = self.get_similar()
        print('indices',indices)
        print('titles',titles)
        idx = indices.loc['The Godfather', 'indices']
        sim_scores = list(enumerate(model[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        return titles.iloc[movie_indices].to_json()