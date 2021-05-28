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


class CurrentGoalWeekAdmin(admin.ModelAdmin):
    list_display = [
        'week_start_date',
        'id',
        'gd1_run',
        'gd1_water',
        'gd1_smoothie',
        'gd1_read',
        'day1_is_complete',
        'gd1_extra_point',
        'gd2_run',
        'gd2_water',
        'gd2_smoothie',
        'gd2_read',
        'day2_is_complete',
        'gd1_extra_point',
        'gd3_run',
        'gd3_water',
        'gd3_smoothie',
        'gd3_read',
        'day3_is_complete',
        'gd1_extra_point',
        'gd4_run',
        'gd4_water',
        'gd4_smoothie',
        'gd4_read',
        'day4_is_complete',
        'gd1_extra_point',
        'gd5_run',
        'gd5_water',
        'gd5_smoothie',
        'gd5_read',
        'day5_is_complete',
        'gd5_extra_point',
        'week_extra_2points',
    ]

admin.site.register(CurrentGoalWeek, CurrentGoalWeekAdmin)
admin.site.register(CurrentGoalDay, CurrentGoalDayAdmin)
admin.site.register(GoalItem, GoalItemAdmin)

admin.site.register(User)

admin.site.register(Agent)

admin.site.register(DayOne)



# adding this to test something