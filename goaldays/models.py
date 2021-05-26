from django.db import models
from goal_item.models import CurrentGoalWeek, GoalItem, Agent


class GoalDayOne(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE, related_name="day_ones_goal_week")
    gd1_run = models.BooleanField(default=False)
    gd1_water = models.BooleanField(default=False)
    gd1_smoothie = models.BooleanField(default=False)
    gd1_read = models.BooleanField(default=False)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #1)'


class GoalDayTwo(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    gd2_run = models.BooleanField(default=False)
    gd2_water = models.BooleanField(default=False)
    gd2_smoothie = models.BooleanField(default=False)
    gd2_read = models.BooleanField(default=False)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #2)'


class GoalDayThree(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    gd3_run = models.BooleanField(default=False)
    gd3_water = models.BooleanField(default=False)
    gd3_smoothie = models.BooleanField(default=False)
    gd3_read = models.BooleanField(default=False)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #3)'


class GoalDayFour(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    gd4_run = models.BooleanField(default=False)
    gd4_water = models.BooleanField(default=False)
    gd4_smoothie = models.BooleanField(default=False)
    gd4_read = models.BooleanField(default=False)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #4)'


class GoalDayFive(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    gd5_run = models.BooleanField(default=False)
    gd5_water = models.BooleanField(default=False)
    gd5_smoothie = models.BooleanField(default=False)
    gd5_read = models.BooleanField(default=False)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #5)'


