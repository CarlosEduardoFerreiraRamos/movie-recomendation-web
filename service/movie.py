from util import DataManager as dm

class MovieRecomender(object):
    
    def predict(self, title):
        return self.get_recommendations(title)

    def get_similar(self):
        dm.get_similar('model')

    def get_ref_files(self):
        return dm.get_csv('indices'), dm.get_csv('titles')

    def get_recommendations(self,title):
        indices, titles = self.get_ref_files()
        model = self.get_similar()
        idx = indices[title]
        sim_scores = list(enumerate(model[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:31]
        movie_indices = [i[0] for i in sim_scores]
        return titles.iloc[movie_indices]