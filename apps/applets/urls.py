from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/authorize', views.Authorize.as_view()),
    path('/login', views.LoginView.as_view())
]