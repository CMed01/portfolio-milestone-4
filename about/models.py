from django.db import models

# Create your models here.

class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title