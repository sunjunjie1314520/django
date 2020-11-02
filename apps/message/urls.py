from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/sms', views.SmsView.as_view()),
    path('/send', views.SendView.as_view()),
    path('/signature', views.SignatureView.as_view()),
    path('/history', views.VisitHistoryView.as_view()),
]