from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Workout(models.Model):
    """
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="workout_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    workout = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class WorkoutComment(models.Model):
    """
    """
    post = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="workout_comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="scorer"
        )
    workout_comment = models.TextField()
    score_number = models.IntegerField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Athlete score: {self.score_number} reps by {self.author}"
        