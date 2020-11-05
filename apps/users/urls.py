from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/login', views.LoginView.as_view()),
    path('/personal', views.PersonalView.as_view()),
    path('/register', views.RegisterView.as_view()),
    path('/modify/<int:pk>', views.ModifyUserDataView.as_view()),
]