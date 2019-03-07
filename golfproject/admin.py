from django.contrib import admin
from golfproject.models import UserProfile, Tournament, BookingModel

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Tournament)
admin.site.register(BookingModel)

