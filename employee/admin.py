from django.contrib import admin
from employee.models import EmployeePersonalInfo, NextOfKind, AreaOfResidence
# Register your models here.
admin.site.register(EmployeePersonalInfo)
admin.site.register(NextOfKind)
admin.site.register(AreaOfResidence)


