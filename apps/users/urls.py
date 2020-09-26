from django.urls import path, include
from .views import Index, Demo

urlpatterns = [
    path('', Index),
    path('login', Demo),
]