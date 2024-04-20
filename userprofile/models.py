from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from workout.models import Workout, WorkoutComment
# Create your models here.

class Profile(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    profile_image = CloudinaryField('image', default='placeholder')