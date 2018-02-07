from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    """This creates a user profile after each user is created, and doesn't do
    anything for subsequent saves to that User object

    This signal is initialized in .apps.AccountConfig.ready()
    """
    Profile.objects.get_or_create(user=instance)
