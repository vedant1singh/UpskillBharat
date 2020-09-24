from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name= "register"),
    path("student_register/", views.student_register.as_view(), name= "student_register")
]