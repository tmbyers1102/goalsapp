from .models import CurrentGoalWeek
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CurrentGoalWeek)
def make_day_complete(sender, instance, created, **kwargs):
    # checks if d1 goals are completed and if so it mark the bool true
    d1_goals_met=False
    d1_goals_total = 0
    d1_goal_list=[
        instance.gd1_run,
        instance.gd1_water,
        instance.gd1_smoothie,
        instance.gd1_read,
    ]
    for x in d1_goal_list:
        if x == True:
            d1_goals_total += 1
    print(str('@@SIGNALS@@: all_goals_total: ') + str(d1_goals_total))
    if d1_goals_total == 4:
        d1_goals_met=True
        print('@@SIGNALS@@: d1_goals_met switched to True')
    else:
        pass
        print('@@SIGNALS@@: DID NOT MEET CRITERIA FOR d1_completed SWITCH')

    if not created:
        print('@@SIGNALS@@: this signal fires on an update but not a newly created instance')
        print(instance)
        if d1_goals_met:
            CurrentGoalWeek.objects.filter(week_start_date=str(instance)).update(day1_is_complete=True)
            print('@@SIGNALS@@: day1_is_complete switched to True')
    else:
        print('@@SIGNALS@@: this shows because its a newly created instance or doesnot qualify to have the complete field switched')


    # Checks if instance is eligible for the 100% end of week extra point
    all_goals_met=False
    all_goals_total = 0
    goal_list=[
        instance.gd1_run,
        instance.gd1_water,
        instance.gd1_smoothie,
        instance.gd1_read,
        instance.gd2_run,
        instance.gd2_water,
        instance.gd2_smoothie,
        instance.gd2_read,
        instance.gd3_run,
        instance.gd3_water,
        instance.gd3_smoothie,
        instance.gd3_read,
        instance.gd4_run,
        instance.gd4_water,
        instance.gd4_smoothie,
        instance.gd4_read,
        instance.gd5_run,
        instance.gd5_water,
        instance.gd5_smoothie,
        instance.gd5_read,
    ]
    for x in goal_list:
        if x == True:
            all_goals_total += 1
    print(str('@@SIGNALS@@: all_goals_total: ') + str(all_goals_total))
    if all_goals_total == 20:
        all_goals_met=True
        print('@@SIGNALS@@: all_goals_met switched to True')
    else:
        pass
        print('@@SIGNALS@@: DID NOT MEET CRITERIA FOR ALL_GOALS SWITCH')

    if not created:
        print('@@SIGNALS@@: this signal fires on an update but not a newly created instance')
        print(instance)
        if all_goals_met:
            CurrentGoalWeek.objects.filter(week_start_date=str(instance)).update(week_extra_2points=True)
            print('week_extra_points switched to True')
    else:
        print('@@SIGNALS@@: this shows because its a newly created instance or doesnot qualify to have the complete field switched')
