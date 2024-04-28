from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from workout.models import Workout, WorkoutComment


class Profile(models.Model):
    """Create Profile Modal
    
    Stores a user profile data related to :model:`auth.User`.
    """
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
