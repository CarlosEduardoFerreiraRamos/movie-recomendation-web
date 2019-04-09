import time
class Tasks(object):
    def __init__(self, celery_intance = None):
        self.celery = celery_intance

    def set_celery(self, celery_intance):
        self.celery = celery_intance

    def create_tasks(self):
        app = self.celery

        @app.task(bind=True)
        def add(self,x, y):
            time.sleep(5)
            return 'FROM CELERY METHOD'

        
