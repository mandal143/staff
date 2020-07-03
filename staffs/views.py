from django.http import HttpResponse
from rest_framework import viewsets
from .models import Employees, LoginLogoutLog
from .serializers import EmployeesSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
    
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
