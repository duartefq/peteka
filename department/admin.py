from django.contrib import admin

# Register your models here.
from department.models import Employee, Document

class EmployeeAdmin(admin.ModelAdmin):
	fields = ['name', 'email', 'password', 'supervisors', 'subordinates']


admin.site.register(Employee, EmployeeAdmin)
