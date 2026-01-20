from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "empcode": forms.TextInput(attrs={"class": "form-control"}),
            "ename": forms.TextInput(attrs={"class": "form-control"}),
            "hname": forms.TextInput(attrs={"class": "form-control"}),
            "designation": forms.TextInput(attrs={"class": "form-control"}),
            "gazet": forms.Select(attrs={"class": "form-select"}),  # if it's a choice field
        }
