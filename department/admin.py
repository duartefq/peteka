from django.contrib import admin

# Register your models here.
from department.models import Employee, Document

class EmployeeAdmin(admin.ModelAdmin):
	fields = ['name', 'email', 'password', 'supervisor']

class DocumentAdmin(admin.ModelAdmin):
	fields = ['title', 'instructions', 'request_date', 'due_date', 'situation', 'approved', 'pdf', 'responsible', 'requester']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Document, DocumentAdmin)

