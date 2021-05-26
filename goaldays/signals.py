from goal_item.models import CurrentGoalWeek, GoalItem
from django.db.models.signals import post_save, m2m_changed
# from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import GoalDayOne, GoalDayTwo, GoalDayThree, GoalDayFour, GoalDayFive


@receiver(post_save, sender=CurrentGoalWeek)
def create_goal_days(sender, instance, created, **kwargs):
    if created:
        GoalDayOne.objects.create(goal_week=instance)
        print('@--`--/-- created day #1')
        # print(CurrentGoalWeek.choose_goals)
        # the_week = [CurrentGoalWeek.choose_goals.through(pk = instance.id)]
        # for x in the_week:
        #     print(str(x))
        GoalDayTwo.objects.create(goal_week=instance)
        print('@--`--/-- created day #2')
        GoalDayThree.objects.create(goal_week=instance)
        print('@--`--/-- created day #3')
        GoalDayFour.objects.create(goal_week=instance)
        print('@--`--/-- created day #4')
        GoalDayFive.objects.create(goal_week=instance)
        print('@--`--/-- created day #5')


# @receiver(post_save, sender=CurrentGoalWeek)
# def save_day_one(sender, instance, **kwargs):
#     print('updated day #1')
#     instance.goaldayone.save()


# create Signal that listens for when a model.CurrentGoalWeek is created and grabs the CurrentGoalWeek.choose_goals from within and then creates a model.GoalInstance for days 1-5 of that week
# with names like run_may_23_to_may_29_day_1 & run_may_23_to_may_29_day_2 & run_may_23_to_may_29_day_3 etc 



 