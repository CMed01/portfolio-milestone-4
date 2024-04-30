from django import forms
from .models import WorkoutComment


class WorkoutcommentForm(forms.ModelForm):
    """Creates Form from WorkoutComment Modal"""
    class Meta:
        model = WorkoutComment
        fields = ('workout_comment', 'score_number',)
