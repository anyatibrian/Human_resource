from django.contrib import admin
from employee.models import EmployeePersonalInfo, NextOfKind, AreaOfResidence
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(EmployeePersonalInfo)
class EmployeePersonalInfoAdmin(ImportExportModelAdmin):
    pass
@admin.register(NextOfKind)
class NextOfKindAdmin(ImportExportModelAdmin):
    pass
@admin.register(AreaOfResidence)
class AreaOfResidenceAdmin(ImportExportModelAdmin):
    pass






