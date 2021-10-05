from django.db.models.signals import post_save
from .models import CustomUser, Profile
from django.dispatch import receiver


@receiver(post_save, sender=CustomUser)
def build_profile_on_user_creation(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()