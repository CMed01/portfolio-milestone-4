from django import forms
from .models import WorkoutComment


class WorkoutcommentForm(forms.ModelForm):
    class Meta:
        model = WorkoutComment
        fields = ('workout_comment', 'score_number',)
        