from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/image', views.ImageView.as_view()),
]