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


class CurrentGoalWeekModelForm(forms.ModelForm):
    class Meta:
        model = CurrentGoalWeek
        fields = (
            'week_start_date',
            'week_end_date',
        )