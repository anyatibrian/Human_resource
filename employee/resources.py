from import_export import resources
from employee.models import (
    EmployeePersonalInfo,
    BankInformation,
    NextOfKind,
    AreaOfResidence,
    EmploymentInformation,
    CitizenshipInfo
)

class EmployeeResourse(resources.ModelResource):
    class Meta:
        model = EmployeePersonalInfo()