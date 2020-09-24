from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Employee
from django.db import transaction
from django import forms
class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_student = True

        user.first_name = self.changed_data.get("first_name")
        user.last_name = self.changed_data.get("last_name")
        user.save()
        student = Student.objects.create(user= user)
        student.phone_number= self.cleaned_data.get('phone_number')
        student.save()
        return student



class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.first_name = self.changed_data.get("first_name")
        user.last_name = self.changed_data.get("last_name")
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.save()
        return employee