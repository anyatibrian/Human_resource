from import_export import resources
from .models import (
                        EmployeePersonalInfo, 
                        EmploymentInformation,
                        CitizenshipInfo,
                        NextOfKind,
                        BankInformation,
                        AreaOfResidence
                    )

# class PersonResource(resources.ModelResource):
#     class Meta:
#         model = P

class EmployeePersonalInfoResource(resources.ModelResource):
    class Meta:
        model = EmployeePersonalInfo
        
class EmploymentInformationResource(resources.ModelResource):
    class Meta:
        model = EmploymentInformation
        
class CitizenshipInfoResource(resources.ModelResource):
    class Meta:
        model = CitizenshipInfo

class NextOfKindResource(resources.ModelResource):
    class Meta:
        model = NextOfKind
class BankInformationResource(resources.ModelResource):
    class Meta:
        model = BankInformation
class AreaOfResidenceResource(resources.ModelResource):
    class Meta:
        model = AreaOfResidence