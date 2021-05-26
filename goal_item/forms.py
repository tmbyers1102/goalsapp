from django import forms
from .models import GoalItem


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