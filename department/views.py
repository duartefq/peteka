from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login #authentication lib

from department.models import Employee, Document

APP = 'department/'

def index(request):
	if request.POST:
		username = request.POST["username"]
		password = request.POST["password"]
		return HttpResponse(username+"<br/>"+password)
	else:
		return render(request, APP+'login.html')
	
