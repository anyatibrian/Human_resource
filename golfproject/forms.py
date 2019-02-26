from django import forms
from django.contrib.auth.models import User
from golfproject.models import UserProfile, Tournament, BookingModel
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class RegisterMember(UserCreationForm):
    """form class responsible for registering members of the club"""

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # meta class responsible for handling the model
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterMember, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_id = 'register-form'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            Submit('submit', 'Save Changes', css_class='btn btn-warning')
        )


class EditProfile(forms.ModelForm):
    """ this form class enables user to edit their profile"""

    class Meta:
        email = forms.EmailField()
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    """form class the enables users to add additional profile information"""
    MEMBER_CHOICES = [
        ('full', 'Full'),
        ('single', 'Single'),
        ('married', 'Married'),
        ('junior', 'Junior'),
        ('cooperate', 'Cooperate'),
        ('Probation', 'Probation')
    ]
    member_category = forms.ChoiceField(required=True, choices=MEMBER_CHOICES)
    GENDER = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(
        required=True,
        choices=GENDER
    )

    class Meta:
        model = UserProfile
        fields = ['gender', 'address', 'phone_number', 'member_category', 'image']


class DateInput(forms.DateInput):
    input_type = 'date'


class TournamentForm(forms.ModelForm):
    state_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())

    class Meta:
        model = Tournament
        fields = ['name',
                  'state_date',
                  'end_date',
                  'booking_fee',
                  'images',
                  'description',
                  'venue'
                  ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'tournament'}),
            'booking_fee': forms.TextInput(attrs={'placeholder': '00000$'})
        }

    def __init__(self, *args, **kwargs):
        super(TournamentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            'name',
            'state_date',
            'end_date',
            'booking_fee',
            'images',
            'description',
            'venue',
            Submit('submit', 'Save Changes', css_class='btn btn-warning float-right')
        )


# the booking forms for matches
class BookingForms(forms.ModelForm):
    TIME_CHOICES = (('8:30', '8:30'), ('8:40', '8:40'), ('8:50', '8:50'))
    tea_time = forms.ChoiceField(choices=TIME_CHOICES)
    # the handicap choices for men's games
    MEN_HANDICAP_CHOICES = (('H-0', 'H-0'), ('H-1', 'H-1'), ('H-2', 'H-2'),
                        ('H-3', 'H-3'), ('H-3', 'H-3'), ('H-4', 'H-4'),
                        ('H-5', 'H-5'), ('H-5', 'H-5'), ('H-6', 'H-6'),
                        ('H-7', 'H-7'), ('H-8', 'H-8'), ('H-9', 'H-9'),
                        ('H-10', 'H-10'), ('H-11', 'H-11'), ('H-12', 'H-13'),
                        ('H-13', 'H-14'), ('H-15', 'H-15'), ('H-16', 'H-16'),
                        ('H-17', 'H-17'), ('H-18', 'H-18'), ('H-20', 'H-20'),
                        ('H-21', 'H-21'), ('H-22', 'H-22'), ('H-23', 'H-23'),
                        ('H-24', 'H-24'), ('H-25', 'H-25'), ('H-26', 'H-26'),
                        ('H-26', 'H-26'), ('H-27', 'H-27'), ('H-28', 'H-28'))
    # the handicap choices for women's games
    WOMEN_HANDICAP_CHOICES = (('H-0', 'H-0'), ('H-1', 'H-1'), ('H-2', 'H-2'),
                        ('H-3', 'H-3'), ('H-3', 'H-3'), ('H-4', 'H-4'),
                        ('H-5', 'H-5'), ('H-5', 'H-5'), ('H-6', 'H-6'),
                        ('H-7', 'H-7'), ('H-8', 'H-8'), ('H-9', 'H-9'),
                        ('H-10', 'H-10'), ('H-11', 'H-11'), ('H-12', 'H-13'),
                        ('H-13', 'H-14'), ('H-15', 'H-15'), ('H-16', 'H-16'),
                        ('H-17', 'H-17'), ('H-18', 'H-18'), ('H-20', 'H-20'),
                        ('H-21', 'H-21'), ('H-22', 'H-22'), ('H-23', 'H-23'),
                        ('H-24', 'H-24'), ('H-25', 'H-25'), ('H-26', 'H-26'),
                        ('H-26', 'H-26'), ('H-27', 'H-27'), ('H-28', 'H-28'),
                        ('H-29', 'H-29'), ('H-30', 'H-30'), ('H-31', 'H-31'),
                        ('H-32', 'H-32'), ('H-33', 'H-33'), ('H-34', 'H-34'),
                        ('H-35', 'H-35'), ('H-36', 'H-36'))

    men_handicap = forms.ChoiceField(label="men's handicap",
                                     choices=MEN_HANDICAP_CHOICES,
                                     required=False)
    women_handicap = forms.ChoiceField(label="women's handicap",
                                       choices=WOMEN_HANDICAP_CHOICES,
                                       required=False)

    class Meta:
        model = BookingModel
        fields = ['user', 'tournament', 'tea_time', 'play_levels', 'men_handicap', 'women_handicap']
        widgets = {
            'user': forms.HiddenInput(attrs={'hidden': True}),
            'tournament': forms.HiddenInput(attrs={'hidden': True}),
            'play_levels': forms.Select(attrs={'required': False})
        }
