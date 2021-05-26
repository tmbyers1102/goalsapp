from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


class User(AbstractUser):
    pass


class GoalItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    value = models.PositiveSmallIntegerField(default=1)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    date_of_goal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class CurrentGoalWeek(models.Model):
    week_start_date = models.DateField(auto_now_add=False)
    week_end_date = models.DateField(auto_now_add=False)
    choose_goals = models.ManyToManyField(GoalItem, blank=True, related_name=('choose_goals'))

    def __str__(self):
        return f'{self.week_start_date} --> {self.week_end_date}'


# class GoalList(models.Model):
#     associated_week = models.models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE, related_name="goal_week")

    
class CurrentGoalDay(models.Model):
    week_day = models.PositiveSmallIntegerField()
    goal_week = models.ForeignKey(CurrentGoalWeek, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.goal_week} (day {self.week_day})'


# create GoalInstance that chooses from types of GoalItem and takes a unique name by attaching it to a CurrentGoalWeek
# class GoalInstance(models.Model):
#     assigned_week = models.ForeignKey(CurrentGoalWeek, on_delete=models.DO_NOTHING)
#     goal_item_type = models.ForeignKey(GoalItem, on_delete=models.DO_NOTHING)



class DayOne(models.Model):
    goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE, related_name="goal_week")
    day_is_complete = models.BooleanField(default=False)
    day_one_goals = models.ManyToManyField(GoalItem, blank=True)

    def __str__(self):
        return f'{self.goal_week} (Day #1)'


@receiver(post_save, sender=CurrentGoalWeek)
def create_days(sender, instance, created, **kwargs):
    if created:
        DayOne.objects.create(
            goal_week = instance,
        )
        print(instance)
        print('?&?&?&?&?&   created new DayOne  ?&?&?&?&?&?&?&&?')


@receiver(m2m_changed, sender=CurrentGoalWeek.choose_goals.through)
def add_the_goals(sender, instance, action, **kwargs):
    if action:
        # goal_list = instance.objects.get()
        # DayOne.objects.update(instance)
        print('<<<<<<<<<<<<<<<   m2m_changed reciever went through >>>>>>>>>>>>>>>>>>')
        print(instance)



# class DayTwo(models.Model):
#     goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
#     day_is_complete = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.goal_week} (Day #2)'


# class DayThree(models.Model):
#     goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
#     day_is_complete = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.goal_week} (Day #3)'


# class DayFour(models.Model):
#     goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
#     day_is_complete = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.goal_week} (Day #4)'


# class DayFive(models.Model):
#     goal_week = models.OneToOneField(CurrentGoalWeek, on_delete=models.CASCADE)
#     day_is_complete = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.goal_week} (Day #5)'