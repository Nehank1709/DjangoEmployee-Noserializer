from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from employee import views

urlpatterns = [
    url("employee_list/", views.ListEmployee.as_view()),
    url("employee_create/", views.UpsertEmployee.as_view()),
    url("employee_delete/", views.DeleteEmployee.as_view()),
]