from django.db import models
import datetime



class Employees(models.Model):

    emp_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=2500, unique=True, default='')
    real_name = models.CharField(max_length=2500, unique=True, default='')
    time_zone_values = (('Africa/Abidjan', 'Africa/Abidjan'), ('America/Los_Angeles', 'America/Los_Angeles'),('Asia/Kolkata', 'Asia/Kolkata'))
    tz = models.CharField(max_length=50, choices=time_zone_values, default='Asia/Kolkata')
    
    
    def __str__(self):
        return str(self.real_name)

class LoginLogoutLog(models.Model):

    login_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
	
    def __str__(self):
	    return str(self.employee)