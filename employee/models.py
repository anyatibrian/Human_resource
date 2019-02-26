from django.db import models
from django.urls import reverse


class EmployeePersonalInfo(models.Model):
    MARITAL_STATUS = (('single', 'single'),
                      ('married', 'married'),
                      ('divorced', 'divorced'),
                      ('cohabiting', 'cohabiting'))
    GENDER = (('male', 'Male'), ('female', 'Female'))
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=100, choices=GENDER)
    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS)
    Contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number_of_children = models.IntegerField()
    image = models.ImageField(default='avatar.jpg', upload_to='media/profile_pic', null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'employee {}'.format(self.first_name)

    # redirect after the updating employee information
    def get_absolute_url(self):
        return reverse('employee-personal-info')


# the model responsible for handling the next of kind information
class NextOfKind(models.Model):
    GENDER = (('male', 'Male'), ('female', 'Female'))
    RELATIONSHIP = (('sister', 'sister'), ('brother', 'brother'), ('wife', 'wife'),
                    ('nephew', 'nephew'), ('niece', 'niece'), ('mother', 'mother'),
                    ('father', 'father'), ('godFather', 'godFather'), ('cousin', 'cousin'),
                    ('inlaw', 'inlaw'))
    employee = models.ForeignKey(EmployeePersonalInfo, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER)
    relationship = models.CharField(max_length=100, choices=RELATIONSHIP)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return '{} personal Information'.format(self.employee.first_name)

    # the redirect for after the form updating
    def get_absolute_url(self):
        return reverse('next-of-kind-info')


# model that handles the employee place of residence
class AreaOfResidence(models.Model):
    employee = models.ForeignKey(EmployeePersonalInfo, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100)
    town_council = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    length_of_current_residence = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.street_name)

    def get_absolute_url(self):
        return reverse('residential-info')


# the model responsible for handling employment details
class EmploymentInformation(models.Model):
    employee = models.ForeignKey(EmployeePersonalInfo, on_delete=models.CASCADE)
    date_employed = models.DateTimeField()
    current_job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    employee_Id_number = models.CharField(max_length=100)
    NSSF_number = models.CharField(max_length=30, null=True)
    Tin_number = models.CharField(max_length=30, null=True)

    def __str__(self):
        return '{} started working on {}'.format(self.employee.first_name, self.date_employed)

    def get_absolute_url(self):
        return reverse('employment-info')


# the models that is responsible for handling the employee bank details
class BankInformation(models.Model):
    employee = models.ForeignKey(EmployeePersonalInfo, on_delete=models.CASCADE, null=True)
    name_of_bank = models.CharField(max_length=100, null=True)
    bank_account_title = models.CharField(max_length=100, null=True)
    account_number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{}'.format(self.name_of_bank)

    def get_absolute_url(self):
        return reverse('employee-bank-info')


# the class responsible for handling citizenship information
class CitizenshipInfo(models.Model):
    employee = models.ForeignKey(EmployeePersonalInfo, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{}'.format(self.country)

    def get_absolute_url(self):
        return reverse('citizenship-info')
