from django.db import models
from goal_item.models import CurrentGoalWeek, GoalItem, Agent


class GoalDayOne(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE, related_name="day_ones_goal_week")
    day_is_complete = models.BooleanField(default=False)
    # goal_day_one_goals = 

    def __str__(self):
        return f'{self.goal_week} (Day #1)'


class GoalDayTwo(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #2)'


class GoalDayThree(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #3)'


class GoalDayFour(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #4)'


class GoalDayFive(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
    day_is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.goal_week} (Day #5)'


