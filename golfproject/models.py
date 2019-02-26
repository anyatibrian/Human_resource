from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save

from Golf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your models here.that can be even use as our billing profile during making bookings
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(max_length=100, default='male')
    address = models.CharField(max_length=100, default='kamapala')
    phone_number = models.CharField(max_length=100)
    member_category = models.CharField(max_length=100)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}profile'


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    state_date = models.DateField()
    end_date = models.DateField()
    booking_fee = models.CharField(max_length=60)
    images = models.ImageField(default='golf', upload_to='images')
    description = models.TextField(max_length=300, default='please enter the tournament description here')
    venue = models.CharField(max_length=100, default='entebbe golf club')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# the model for booking a match
class BookingModel(models.Model):
    PLAY_CHOICES = (
        ('professional', 'professional'),
        ('Handicap', 'Handicap')
    )
    HANDICAP_LEVELS = (('men', 'men'), ('women', 'women'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    tea_time = models.TimeField()
    create_at = models.DateTimeField(auto_now_add=True)
    play_type = models.CharField(max_length=20, choices=PLAY_CHOICES, null=True, default='professional')
    play_levels = models.CharField(max_length=20, choices=PLAY_CHOICES, null=True, default='professional')
    Handicaps = models.CharField(max_length=20, choices=HANDICAP_LEVELS, null=True, default='men')
    men_handicap = models.CharField(max_length=20, null=True)
    women_handicap = models.CharField(max_length=20, null=True, default="None")

    def __str__(self):
        return f'{self.tournament} booking'


