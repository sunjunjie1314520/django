from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class ApiConfig(AppConfig):
    name = 'api'

    # def ready(self):
        # super().ready()
        # autodiscover_modules('xxx')
