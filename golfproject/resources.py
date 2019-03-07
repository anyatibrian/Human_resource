from import_export import resources
from .models import BookingModel, UserProfile, Tournament

class BookingModelResource(resources.ModelResource):
    class Meta:
        model = BookingModel

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile

class TournamentResource(resources.ModelResource):
    class Meta:
        model = Tournament