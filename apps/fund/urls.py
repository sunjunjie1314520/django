
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/search', views.SearchListView.as_view()),
    path('/realtime', views.RealtimeListView.as_view()),
]
