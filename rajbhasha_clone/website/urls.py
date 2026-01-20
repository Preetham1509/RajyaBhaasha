from django.urls import path
from .views import (
    home,
    employee_form,
    EmployeeListCreateAPI,
    EmployeeDetailAPI
)

urlpatterns = [
    # Frontend
    path('', home, name='home'),
    path('employee-form/', employee_form, name='employee_form'),

    # API
    path('api/employees/', EmployeeListCreateAPI.as_view(), name='employee_list_create'),
    path('api/employees/<int:pk>/', EmployeeDetailAPI.as_view(), name='employee_detail'),
]
