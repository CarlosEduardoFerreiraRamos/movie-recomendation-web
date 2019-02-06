from sklearn.externals.joblib import dump, load
import pandas as pd

MODEL_PATH = 'assets/models/'

FILE_PATH = 'assets/files/'

class DataManager(object):
    pass

    @staticmethod
    def get_csv(self, file_name):
        full_path = FILE_PATH + file_name + '.csv'
        return pd.read_csv(full_path)

    @staticmethod
    def get_model(self, file_name):
        full_path = MODEL_PATH + file_name + '.joblib'
        return load(full_path)