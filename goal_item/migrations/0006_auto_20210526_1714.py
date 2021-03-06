# Generated by Django 3.1.7 on 2021-05-26 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goal_item', '0005_auto_20210524_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayone',
            name='day_one_goals',
            field=models.ManyToManyField(blank=True, to='goal_item.GoalItem'),
        ),
        migrations.AlterField(
            model_name='dayone',
            name='goal_week',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='goal_week', to='goal_item.currentgoalweek'),
        ),
    ]
