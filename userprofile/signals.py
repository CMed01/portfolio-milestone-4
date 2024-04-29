from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)

def create_profile(sender, instance, created, **kwargs):
    """Create profile when new user registers"""
    if created:
        Profile.objects.create(author=instance, slug=instance)
        