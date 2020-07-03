from django.urls import path, include

from . import views
from rest_framework import routers
from .views import EmployeesViewSet

router = routers.DefaultRouter()
router.register(r'', EmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]