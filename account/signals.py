from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile

User = get_user_model()

@receiver(post_save, sender=User)
def manage_user_profile(sender, instance, created, **kwargs):
    if instance.is_email_verified:
        Profile.objects.get_or_create(user=instance)
