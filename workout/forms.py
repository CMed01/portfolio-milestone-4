from .models import WorkoutComment
from django import forms


class WorkoutcommentForm(forms.ModelForm):
    class Meta:
        model = WorkoutComment
        fields = ('workout_comment','score_number',)
        