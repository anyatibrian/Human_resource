from django.shortcuts import render, redirect
from golfproject.forms import (RegisterMember,
                               EditProfile,
                               UserProfileForm,
                               TournamentForm,
                               BookingForms)
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.models import User
from golfproject.models import Tournament, BookingModel, UserProfile
import stripe
from Golf import settings
#update member
from django.views.generic.edit import UpdateView
stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY

STRIPE_PUBLISHABLE_KEY = 'pk_test_yWpgqkKdZ3dGTlNDqmIss0sF'


# function that checks whether the user is supper admin
def admin_index_page(request):
    return render(request, 'golfproject/admin-index.html')


# loafing the login page
def login_page(request):
    return render(request, 'golfproject/pages/samples/login.html')


# the function enables super to register new member
@login_required()
@permission_required('is_superuser')
def create_member_view(request):
    if request.method == 'POST':
        reg_form = RegisterMember(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'members account has been successfully created')
            return redirect('admin-members')
    else:
        reg_form = RegisterMember()
    context = {
        'reg_form':reg_form
    }
    return render(request, 'golfproject/members_create.html', context)


# loading the members page
@login_required()
@permission_required('is_superuser')
def members_page(request):
    if request.method == 'POST':
        register_form = RegisterMember(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'member'+username+'has been created successfully')
            return redirect('admin-members')
    else:
        register_form = RegisterMember()
    context = {
        'members': User.objects.all(),
        'reg_form': register_form
    }

    return render(request, 'golfproject/members.html', context)


# loading the user profile page
@login_required()
def user_profile_page(request):
    if request.method == 'POST':
        profile_form_two = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        profile_form_one = EditProfile(request.POST, instance=request.user)
        if profile_form_two.is_valid() and profile_form_two.is_valid():
            profile_form_two.save()
            profile_form_one.save()
            redirect('admin-profile')
            messages.success(request, 'your profile have been successfully updated')
    else:
        profile_form_two = UserProfileForm(instance=request.user.userprofile)
        profile_form_one = EditProfile(instance=request.user)
    context = {
        'profile_form_two': profile_form_two,
        'profile_form_one': profile_form_one,
    }
    return render(request, 'golfproject/profileUpdate.html', context)


@login_required()
@permission_required('is_superuser')
def add_tournament(request):
    tournaments = Tournament.objects.all()
    if request.method == 'POST':
        tournament_form = TournamentForm(request.POST, request.FILES)
        if tournament_form.is_valid():
            tournament_form.save()
            return redirect('admin-tournament')
    else:
        tournament_form = TournamentForm()
    context = {
        'tournament_form': tournament_form,
        'tournaments': tournaments
    }
    return render(request, 'golfproject/tournament.html', context)


# the view the loads all the tournaments
@login_required()
def view_tournaments(request):
    tournament_list = Tournament.objects.all()
    context = {
        'tournament_list': tournament_list
    }
    return render(request, 'golfproject/tournament_list.html', context)


class TournamentListView(LoginRequiredMixin, ListView):
    model = Tournament
    template_name = 'golfproject/tournament_list.html'
    context_object_name = 'tournament_list'
    ordering = ['created_at']


def tournament_detail(request, tournament_id):
    # creating single post by id
    tournament = Tournament.objects.get(id=tournament_id)
    default_data = {
        'user': request.user.pk,
        'tournament': tournament.pk
    }
    # making a booking form post request
    if request.method == 'POST':
        booking_forms = BookingForms(request.POST, initial=default_data)
        if booking_forms.is_valid():
            booking_forms.save()
            messages.success(request, ' thanks for booking the match')
            return redirect('user-tournaments')
    else:
        booking_forms = BookingForms(initial=default_data)
    context = {
        'booking_forms': booking_forms,
        'tournament': tournament,
        'publish_key': STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'golfproject/tournament_detail.html', context)


# function that fetches all the booking
@login_required()
@permission_required('is_superuser')
def admin_booking_view(request):
    booking_info = BookingModel.objects.all()
    context = {
        'booking_info': booking_info
    }
    return render(request, 'golfproject/admin_booking_details.html', context)


@login_required()
def tournament_detail_view(request):
    booking_info = BookingModel.objects.filter(user=request.user)
    context = {
        'booking': booking_info
    }
    return render(request, 'golfproject/tournament_booking.html', context)


#edit member view

class UpdateMember(UpdateView):
    model = UserProfile
    fields = ['gender', 'address', 'phone_number', 'member_category', 'image']
    template_name = 'golfproject/update_form.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'