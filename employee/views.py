from django.shortcuts import render, redirect,Http404,HttpResponse
from django.urls import reverse_lazy
import django_excel as excel
from employee.models import (EmployeePersonalInfo,
                             NextOfKind,
                             EmploymentInformation,
                             BankInformation,
                             CitizenshipInfo,
                             AreaOfResidence)
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from golfproject.forms import DateInput
from tablib import Dataset
from employee.forms import ImportForm
from employee.resources import (
                                EmployeeInfoResource, 
                                EmploymentInformationResourse,
                                NextOfKindResources,BankInfoResources,
                                CitizenshipResources,
                                AreaOfResidenceResources
                               )


# Create your views here.

@login_required()
@permission_required('is_superuser')
def view_employee_personal_info(request):
    # the view responsible for showing all the employee information details
    employee_info = EmployeePersonalInfo.objects.all()
    if request.method =='POST':
        import_form = ImportForm(request.POST, request.FILES)
        employee_info_resource = EmployeeInfoResource()
        dataset = Dataset()
        new_employee = request.FILES['file']
        dataset.load(new_employee.read())
        result = employee_info_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            employee_info_resource.import_data(dataset, dry_run=False)
    else:
          import_form = ImportForm()                           
    context = {
        'employee_info': employee_info,
        'heading':'choose your file to uplaod',
        'import_form':import_form
    }
    return render(request, 'employee/personal_info.html', context)
# export data from the csv file

def export_employee_info(request):
    employee = EmployeeInfoResource()
    dataset = employee.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def export_employeement_info(request):
    employment_info = EmploymentInformationResourse()
    dataset = employment_info.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="employent_info.xls"'
    return response


def export_next_of_kind_info(request):
    next_of_kind_info = NextOfKindResources()
    dataset = next_of_kind_info.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="nextofkind_info.xls"'
    return response


def export_bank_info(request):
    bank_info = NextOfKindResources()
    dataset = bank_info.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="bank_info.xls"'
    return response


def export_citienship_info(request):
    citizenship = CitizenshipResources()
    dataset = citizenship.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="citizenship_info.xls"'
    return response


def export_areof_residence_info(request):
    area_of_residence = AreaOfResidenceResources()
    dataset = area_of_residence.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="areofresidence_info.xls"'
    return response

class EmployeeInfoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = EmployeePersonalInfo
    fields = ['surname', 'first_name', 'middle_name', 'image', 'date_of_birth',
              'gender', 'marital_status', 'email', 'Contact', 'number_of_children']

    def get_form(self, form_class=CreateView):
        form = super().get_form()
        form.fields['date_of_birth'].widget = DateInput()
        return form

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class EditPersonalDetailView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = EmployeePersonalInfo
    fields = ['surname', 'first_name', 'middle_name', 'image', 'date_of_birth',
              'gender', 'marital_status', 'email', 'Contact', 'number_of_children']

    def get_form(self, form_class=UpdateView):
        form = super().get_form()
        form.fields['date_of_birth'].widget = DateInput()
        return form

    def form_invalid(self, form):
        form.is_valid()
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


""" the section below are basically the views that handles the respective next of kind information of a employee"""


@login_required()
@permission_required('is_superuser')
def view_employee_nextOfKindInfo(request):
    # function that is responsible for viewing all the next of kind detail
    next_of_kind_info = NextOfKind.objects.all()
    context = {
        'next_of_kind_info': next_of_kind_info
    }
    return render(request, 'employee/nextofkind_information.html', context)


class NextOfKindCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """class the is responsible for adding new next of kind detail """
    model = NextOfKind
    fields = ['employee', 'surname', 'first_name', 'gender', 'relationship', 'contact']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class NextOfKindEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """the class that is responsible for editing existing next of kind details"""
    model = NextOfKind
    fields = ['employee', 'surname', 'first_name', 'gender', 'relationship', 'contact']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


""" the view section that handles various employee employment information """


@login_required()
@permission_required('is_superuser')
def view_employee_employment_info(request):
    # function that is responsible for viewing all the next of kind detail
    employment_info = EmploymentInformation.objects.all()
    context = {
        'employment_info': employment_info
    }
    return render(request, 'employee/employmentInfo.html', context)


class EmploymentInfoCreateView(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    """ the class that adds the employee  employment information """
    model = EmploymentInformation
    fields = ['employee', 'date_employed', 'current_job_title', 'department',
              'employee_Id_number', 'Tin_number', 'NSSF_number']

    def get_form(self, form_class=CreateView):
        form = super().get_form()
        form.fields['date_employed'].widget = DateInput()
        return form
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class EmploymentInfoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ the class that adds the employee  employment information """
    model = EmploymentInformation
    fields = ['employee', 'date_employed', 'current_job_title', 'department',
              'employee_Id_number', 'Tin_number', 'NSSF_number']
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class EmploymentInfoDeleteView(DeleteView):
    """ the class responsible for deleting Employment info from the data base"""
    model = EmployeePersonalInfo
    success_url = reverse_lazy('employment-info')
    template_name = 'employee/employmentInfo.html'


""" the view section that handles the employee Bank information Details"""


@login_required()
@permission_required('is_superuser')
def view_bank_info(request):
    # function that is responsible for viewing all the next of kind detail
    bank_info = BankInformation.objects.all()
    context = {
        'bank_info': bank_info
    }
    return render(request, 'employee/bankinfo.html', context)


class BankInfoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ the module responsible for adding the employee banking information"""
    model = BankInformation
    fields = ['employee', 'name_of_bank', 'bank_account_title', 'account_number']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class BankInfoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ the module responsible for adding the employee banking information"""
    model = BankInformation
    fields = ['employee', 'name_of_bank', 'bank_account_title', 'account_number']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


""" the view section that handles employee citizenship information"""


@login_required()
@permission_required('is_superuser')
def view_employee_citizenshipInfo(request):
    citizenship_info = CitizenshipInfo.objects.all()
    context = {
        'citizenship_info': citizenship_info
    }
    return render(request, 'employee/citizenship_info.html', context)


class CitizenshipCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CitizenshipInfo
    fields = ['employee', 'city', 'sub_county', 'district', 'country']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class CitizenshipEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CitizenshipInfo
    fields = ['employee', 'city', 'sub_county', 'district', 'country']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


""" this section of the view handles residential information"""


@login_required()
@permission_required('is_superuser')
def view_employee_residentialInfo(request):
    residential_info = AreaOfResidence.objects.all()
    context = {
        'area_info': residential_info
    }
    return render(request, 'employee/residential_info.html', context)


class ResidentialInfoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = AreaOfResidence
    fields = ['employee', 'street_name', 'town_council', 'district', 'length_of_current_residence']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


class ResidentialInfoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AreaOfResidence
    fields = ['employee', 'street_name', 'town_council', 'district', 'length_of_current_residence']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False


@login_required()
@permission_required('is_superuser')
def employee_profile_view(request, pk):
    employee_info = EmployeePersonalInfo.objects.get(pk=pk)
    context ={
        'employee_info':employee_info
    }
    return render(request, 'employee/employee_profile.html', context)
