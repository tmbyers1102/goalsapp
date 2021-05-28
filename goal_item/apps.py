from django.apps import AppConfig


class GoalItemConfig(AppConfig):
    name = 'goal_item'

    def ready(self): # this makes sure the signals in signals.py work correctly
        import goal_item.signals