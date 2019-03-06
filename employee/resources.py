from import_export import resources, fields, widgets
from import_export.widgets import ForeignKeyWidget
from import_export import resources
from employee.models import (
    EmployeePersonalInfo,
    BankInformation,
    NextOfKind,
    AreaOfResidence,
    EmploymentInformation,
    CitizenshipInfo
)

class EmployeeInfoResource(resources.ModelResource):
    class Meta:
        model = EmployeePersonalInfo
        exclude =('image','create_at')

class EmploymentInformationResourse(resources.ModelResource):
    class Meta:
        model = EmploymentInformation
        employee = fields.Field(column_name='employee', attribute='employee',
                              widget=ForeignKeyWidget(EmployeePersonalInfo,'surname'))
        fields =('employee')


class NextOfKindResources(resources.ModelResource):
    class Meta:
        model = NextOfKind
        employee = fields.Field(column_name='employee', attribute='employee',
                                widget=ForeignKeyWidget(EmployeePersonalInfo, 'surname'))

class BankInfoResources(resources.ModelResource):
    class Meta:
        model = BankInformation
        employee = fields.Field(column_name='employee', attribute='employee',
                                widget=ForeignKeyWidget(EmployeePersonalInfo, 'surname'))


class CitizenshipResources(resources.ModelResource):
    class Meta:
        model = CitizenshipInfo
        employee = fields.Field(column_name='employee', attribute='employee',
                                widget=ForeignKeyWidget(EmployeePersonalInfo, 'surname'))


class AreaOfResidenceResources(resources.ModelResource):
    class Meta:
        model = AreaOfResidence
        employee = fields.Field(column_name='employee', attribute='employee',
                                widget=ForeignKeyWidget(EmployeePersonalInfo, 'surname'))
