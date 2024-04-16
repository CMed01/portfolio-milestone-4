from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Header(models.Model):
    """
    Stores a title and sub title for the landing page
    This is editable
    """
    title = models.CharField(max_length=200, unique=True)
    sub_title = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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