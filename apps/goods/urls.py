
from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/list', views.GoodsListView.as_view()),
]
