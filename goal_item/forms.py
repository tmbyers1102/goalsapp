from django import forms
from .models import CurrentGoalWeek, GoalItem


class GoalItemModelForm(forms.ModelForm):
    class Meta:
        model = GoalItem
        fields = (
            'name',
            'description',
            'value',
            'agent',
            'is_complete'
        )

class DateInput(forms.DateInput):
    input_type = 'date'


class CurrentGoalWeekModelForm(forms.ModelForm):
    class Meta:
        model = CurrentGoalWeek
        widgets = {'week_start_date': DateInput()}
        fields = (
            'week_start_date',
        )





class CurrentGoalWeekUpdateForm(forms.ModelForm):

    class Meta:
        model = CurrentGoalWeek
        fields = [
            'gd1_run',
            'gd1_water',
            'gd1_smoothie',
            'gd1_read',
            'gd2_run',
            'gd2_water',
            'gd2_smoothie',
            'gd2_read',
            'gd3_run',
            'gd3_water',
            'gd3_smoothie',
            'gd3_read',
            'gd4_run',
            'gd4_water',
            'gd4_smoothie',
            'gd4_read',
            'gd5_run',
            'gd5_water',
            'gd5_smoothie',
            'gd5_read'
        ]