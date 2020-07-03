from rest_framework import serializers
from .models import Employees, LoginLogoutLog      


class LoginLogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginLogoutLog
        fields = ['start_time', 'end_time']
        
        
class EmployeesSerializer(serializers.ModelSerializer):
    activity_periods = LoginLogoutSerializer(many=True)
    
    class Meta:
        model = Employees
        fields = ['id', 'real_name','tz','activity_periods']


        
        
