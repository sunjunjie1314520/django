
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/search', views.SearchListView.as_view()),
    path('/realtime', views.RealtimeListView.as_view()),
    path('/sort', views.SortView.as_view()),
    path('/set_top', views.SetTopView.as_view()),
]
