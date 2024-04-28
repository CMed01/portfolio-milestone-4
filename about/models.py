from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class About(models.Model):
    """
    Stores content for display on the landing page that provides the user information 
    about the owner and purpose of websote.
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    profile_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    """
    Stores content for display on the landing page that provides the user information 
    about the owner and purpose of websote.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
