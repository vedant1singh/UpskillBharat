from django.shortcuts import render
from django.views.generic import CreateView
from .models import User, Student, Employee
from .form import StudentSignUpForm, EmployeeSignUpForm
def register(request):
    return render(request, "register.html")

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = "student_register.html"
