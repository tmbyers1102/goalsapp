# Generated by Django 3.1.7 on 2021-05-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goal_item', '0006_auto_20210526_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentgoalweek',
            name='day1_is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='day2_is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='day3_is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='day4_is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='day5_is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd1_extra_point',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd1_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd1_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd1_smoothie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd1_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd2_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd2_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd2_smoothie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd2_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd3_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd3_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd3_smoothie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd3_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd4_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd4_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd4_smoothie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd4_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd5_extra_point',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd5_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd5_run',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd5_smoothie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='gd5_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='currentgoalweek',
            name='week_extra_2points',
            field=models.BooleanField(default=False),
        ),
    ]
