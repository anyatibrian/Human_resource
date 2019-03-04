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
