from django.contrib import admin

from .models import Employees, LoginLogoutLog

admin.site.register(Employees)
admin.site.register(LoginLogoutLog)