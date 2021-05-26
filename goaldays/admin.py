from django.contrib import admin
from . models import GoalDayOne, GoalDayTwo, GoalDayThree, GoalDayFour, GoalDayFive

class GoalDayOneAdmin(admin.ModelAdmin):
    list_display = [
        'goal_week',
        'gd1_run',
        'gd1_water',
        'gd1_smoothie',
        'gd1_read',
        'day_is_complete',
    ]


class GoalDayTwoAdmin(admin.ModelAdmin):
    list_display = [
        'goal_week',
        'gd2_run',
        'gd2_water',
        'gd2_smoothie',
        'gd2_read',
        'day_is_complete',
    ]


class GoalDayThreeAdmin(admin.ModelAdmin):
    list_display = [
        'goal_week',
        'gd3_run',
        'gd3_water',
        'gd3_smoothie',
        'gd3_read',
        'day_is_complete',
    ]


class GoalDayFourAdmin(admin.ModelAdmin):
    list_display = [
        'goal_week',
        'gd4_run',
        'gd4_water',
        'gd4_smoothie',
        'gd4_read',
        'day_is_complete',
    ]


class GoalDayFiveAdmin(admin.ModelAdmin):
    list_display = [
        'goal_week',
        'gd5_run',
        'gd5_water',
        'gd5_smoothie',
        'gd5_read',
        'day_is_complete',
    ]


admin.site.register(GoalDayOne, GoalDayOneAdmin)
admin.site.register(GoalDayTwo, GoalDayTwoAdmin)
admin.site.register(GoalDayThree, GoalDayThreeAdmin)
admin.site.register(GoalDayFour, GoalDayFourAdmin)
admin.site.register(GoalDayFive, GoalDayFiveAdmin)
