from celery import Celery
from .config import Config
import pickle

celery_app = Celery('apCelery', broker=Config.BROKER, backend=Config.BACKEND, include=Config.INCLUDE)
celery_app.config_from_object(Config)


class TaskLoader:
    app = celery_app

    def __init__(self, func_name: str, load_type: str, func_code: str, trigger: dict):
        self.func_name = func_name
        self.load_type = load_type
        self.func_code = func_code
        self.trigger = trigger

    def _exec(self) -> None:
        exec(self.func_code)
        pass
