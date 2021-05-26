from django.apps import AppConfig


class GoaldaysConfig(AppConfig):
    name = 'goaldays'

    def ready(self): # this makes sure the signals in signals.py work correctly
        import goaldays.signals