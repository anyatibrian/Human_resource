from django.apps import AppConfig


class GolfprojectConfig(AppConfig):
    name = 'golfproject'

    def ready(self):
        from golfproject import signals
