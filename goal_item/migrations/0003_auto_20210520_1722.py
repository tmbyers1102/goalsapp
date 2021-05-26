# Generated by Django 3.1.7 on 2021-05-20 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goal_item', '0002_goalitem_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalitem',
            name='date_of_goal',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]