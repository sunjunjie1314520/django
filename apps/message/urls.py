from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index),
    path('sms', views.SmsView.as_view()),
    path('send', views.SendView.as_view()),
]