from django.contrib import admin
from . models import GoalItem, User, Agent, CurrentGoalWeek, CurrentGoalDay, DayOne


class CurrentGoalDayAdmin(admin.ModelAdmin):
    list_display = [
        'week_day',
        'goal_week',
    ]
    search_fields = [
        'week_day',
        'goal_week',
    ]


class GoalItemAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'agent',
        'is_complete',
        'date_of_goal'
    ]
    search_fields = [
        'name',
        'agent',
        'is_complete',
        'date_of_goal'
    ]

admin.site.register(CurrentGoalWeek)
admin.site.register(CurrentGoalDay, CurrentGoalDayAdmin)
admin.site.register(GoalItem, GoalItemAdmin)

admin.site.register(User)

admin.site.register(Agent)

admin.site.register(DayOne)
