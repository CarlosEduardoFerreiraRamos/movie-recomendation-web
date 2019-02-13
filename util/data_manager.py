from sklearn.externals.joblib import dump, load
import pandas as pd

MODEL_PATH = 'assets/models/'

FILE_PATH = 'assets/files/'

class DataManager(object):
    pass

    @staticmethod
    def get_csv(file_name, index=None):
        full_path = FILE_PATH + file_name + '.csv'
        return pd.read_csv(filepath_or_buffer=full_path, index_col=index)

    @staticmethod
    def get_model(file_name):
        full_path = MODEL_PATH + file_name + '.joblib'
        return load(full_path)