# apps/users/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile #, NotificationPreference

User = get_user_model()

@receiver(post_delete, sender=Profile, dispatch_uid="Delete profile picture")
def delete_profile_avatar(sender, instance, **kwargs):
    """ Delete avatar from file system if avatar exists """
    import os
    if instance.avatar:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)
            
@receiver(post_save, sender=User, dispatch_uid="Create users profile")
def create_user_profile(sender, instance, created, **kwargs):
    """ Create profile for user """
    '''
    # sender    # the model class that was saved → User
    # instance  # the actual object that was saved → the specific User row
    # created   # True if this was INSERT, False if this was UPDATE
    # kwargs    # extra stuff Django passes, you don't need it but must accept it
    '''
    # If created for the first time
    if created:
        Profile.objects.create(user=instance)
        # NotificationPreference.objects.create(user=instance)