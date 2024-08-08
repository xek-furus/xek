from django.contrib import admin
from django.urls import path
from .import views

app_name = "smart_admin"

urlpatterns = [
     path('dashboard/',views.dashboard, name='dashboard'),
]