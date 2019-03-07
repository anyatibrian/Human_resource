from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from golfproject.models import UserProfile
from golfproject.models import BookingModel
from Golf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


@receiver(signals.post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ the method the creates a user profile each time a user is created"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(signals.post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """ the method responsible for saving each of the user profile"""
    instance.userprofile.save()
