from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path("employee_list/", views.ListEmployee.as_view()),
    path("employee_create/", views.UpsertEmployee.as_view()),
    path("employee_delete/", views.DeleteEmployee.as_view()),
]