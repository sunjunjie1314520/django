from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index),
    path('login', views.LoginView.as_view()),
]